"""Tests for the scripts the skills run. Standard library only.

Run from the repository root: python3 -m unittest discover tests
"""
import json
import subprocess
import sys
import tempfile
import unittest
from datetime import date, timedelta
from pathlib import Path

SKILLS = Path(__file__).resolve().parent.parent / "business-ops" / "skills"
CHECK = SKILLS / "business-context" / "scripts" / "check_context.py"
CALC = SKILLS / "finance" / "scripts" / "finance_calc.py"

CATALOG = """# Acme catalog

## Plans

| ID | Plan | Price | Includes | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| `basic-plan` | Basic plan | 99 per month | up to 10 users | available | |
| `team-plan` | Team plan | 199 per month | up to 50 users | planned | |
"""

TEMPLATE = """---
template: commercial-proposal
company: acme
uses: [{uses}]
---

# Commercial proposal
"""


def run(script, *args, stdin=None):
    return subprocess.run([sys.executable, str(script), *map(str, args)], capture_output=True, text=True, input=stdin)


class ContextFolder(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.write("business-ops-context.md", "# business-ops context\n")
        self.write("acme/context.md", "# Acme context\n\n## Updates\n")
        self.write("acme/catalog.md", CATALOG)
        self.write("acme/templates/commercial-proposal.md", TEMPLATE.format(uses="basic-plan"))

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def check(self, *args):
        return run(CHECK, self.root, *args)

    def test_clean_folder_passes(self):
        result = self.check()
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("0 error(s), 0 warning(s)", result.stdout)

    def test_missing_index_is_an_error(self):
        (self.root / "business-ops-context.md").unlink()
        self.assertEqual(self.check().returncode, 1)

    def test_repeated_id(self):
        self.write("acme/catalog.md", CATALOG + "| `basic-plan` | Again | 1 | | available | |\n")
        result = self.check()
        self.assertEqual(result.returncode, 1)
        self.assertIn("is repeated", result.stdout)

    def test_malformed_id_and_status(self):
        self.write("acme/catalog.md", CATALOG + "| `Big Plan` | Big | 1 | | on sale | |\n")
        result = self.check()
        self.assertIn("must hold one ID", result.stdout)
        self.assertIn("Status cell must start with", result.stdout)

    def test_status_followed_by_a_note_is_accepted(self):
        self.write("acme/catalog.md", CATALOG + "| `extra` | Extra | 1 | | `available`, confirmed in May | |\n")
        self.assertEqual(self.check().returncode, 0)

    def test_template_naming_unknown_id(self):
        self.write("acme/templates/commercial-proposal.md", TEMPLATE.format(uses="basic-plan, gone-plan"))
        result = self.check()
        self.assertEqual(result.returncode, 1)
        self.assertIn("`gone-plan`, which is not an ID", result.stdout)

    def test_template_naming_unavailable_entry_is_a_warning(self):
        self.write("acme/templates/commercial-proposal.md", TEMPLATE.format(uses="team-plan"))
        result = self.check()
        self.assertEqual(result.returncode, 0)
        self.assertIn("whose status is `planned`", result.stdout)

    def test_uses_as_a_block_list(self):
        text = "---\ntemplate: commercial-proposal\ncompany: acme\nuses:\n  - basic-plan\n  - gone-plan\n---\n"
        self.write("acme/templates/commercial-proposal.md", text)
        self.assertIn("`gone-plan`", self.check().stdout)

    def test_history_order_and_ceiling(self):
        old = (date.today() - timedelta(days=800)).isoformat()
        new = date.today().isoformat()
        self.write("acme/changelog.md", f"# Acme changelog\n\n## {old}: first\n\n## {new}: second\n")
        result = self.check()
        self.assertIn("not newest first", result.stdout)
        self.assertIn("past the ceiling", result.stdout)

    def test_uses_lists_templates_and_mentions(self):
        self.write("acme/deliverables/2026-01-05-reply/reply.md", "We recommend the Basic plan.\n")
        self.write("acme/archive/old.md", "Basic plan\n")
        result = self.check("--company", "acme", "--uses", "basic-plan")
        self.assertEqual(result.returncode, 0)
        self.assertIn("templates/commercial-proposal.md", result.stdout)
        self.assertIn("reply.md (lines 1)", result.stdout)
        self.assertNotIn("old.md", result.stdout)

    def test_folder_is_left_unchanged(self):
        before = {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.check()
        self.check("--company", "acme", "--uses", "basic-plan")
        self.assertEqual(before, {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()})


class FinanceCalc(unittest.TestCase):
    def calc(self, *args, stdin=None):
        result = run(CALC, *args, stdin=stdin)
        return result.returncode, json.loads(result.stdout)

    def test_break_even(self):
        code, out = self.calc("break-even", "--fixed-costs", 12000, "--price", 99, "--variable-cost", 22)
        self.assertEqual(code, 0)
        self.assertEqual(out["contribution_margin_per_unit"], 77.0)
        self.assertEqual(out["break_even_units"], 156)
        self.assertEqual(out["break_even_revenue"], 15428.57)

    def test_break_even_exact_volume_is_not_rounded_up(self):
        _, out = self.calc("break-even", "--fixed-costs", 1000, "--price", 20, "--variable-cost", 10)
        self.assertEqual(out["break_even_units"], 100)

    def test_price_below_variable_cost(self):
        code, out = self.calc("break-even", "--fixed-costs", 1000, "--price", 5, "--variable-cost", 9)
        self.assertEqual(code, 1)
        self.assertIn("error", out)

    def test_unit_economics(self):
        code, out = self.calc("unit-economics", "--cac", 450, "--revenue-per-customer", 99, "--gross-margin", 80, "--monthly-churn", 3)
        self.assertEqual(code, 0)
        self.assertEqual(out["ltv"], 2640.0)
        self.assertEqual(out["ltv_to_cac"], 5.87)
        self.assertEqual(out["cac_payback_months"], 5.68)

    def test_zero_churn_is_refused(self):
        code, out = self.calc("unit-economics", "--cac", 450, "--revenue-per-customer", 99, "--gross-margin", 80, "--monthly-churn", 0)
        self.assertEqual(code, 1)
        self.assertIn("churn", out["error"])

    def test_cash_flow_scenarios(self):
        plan = {
            "opening_balance": 20000,
            "months": [
                {"label": "2026-01", "inflows": 30000, "outflows": 34000},
                {"label": "2026-02", "inflows": 32000, "outflows": 34000},
            ],
            "scenarios": {"base": {}, "worst": {"inflows": 80, "outflows": 105}},
        }
        code, out = self.calc("cash-flow", "-", stdin=json.dumps(plan))
        self.assertEqual(code, 0)
        base, worst = out["scenarios"]["base"], out["scenarios"]["worst"]
        self.assertEqual(base["closing_balance"], 14000.0)
        self.assertIsNone(base["first_negative_month"])
        self.assertEqual(worst["closing_balance"], -1800.0)
        self.assertEqual(worst["first_negative_month"], "2026-02")
        self.assertEqual(worst["lowest_balance_month"], "2026-02")

    def test_cash_flow_missing_number(self):
        plan = {"opening_balance": 100, "months": [{"inflows": 10}]}
        code, out = self.calc("cash-flow", "-", stdin=json.dumps(plan))
        self.assertEqual(code, 1)
        self.assertIn("month 1", out["error"])


if __name__ == "__main__":
    unittest.main()
