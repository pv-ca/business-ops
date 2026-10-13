# Histórico de versões

O número da versão fica em `business-ops/.claude-plugin/plugin.json`. Cada agente guarda uma cópia do plugin por versão, então toda mudança nas skills sobe o número.

## 0.7.0 (13/10/2026)

- O catálogo de instalação passou a se chamar `pvca`. O plugin agora é instalado como `business-ops@pvca`.
- Primeiro commit no repositório próprio, com README em português e este histórico.

## 0.6.1 (13/10/2026)

- O plugin deixou de citar qualquer empresa. As seções de adaptação por empresa saíram de três playbooks e foram para o arquivo `adaptacao-dos-metodos.md` da pasta de contexto de cada empresa.
- O protocolo passou a mandar ler esse arquivo antes de aplicar um método.

## 0.6.0 (13/10/2026)

- Nova skill `social-media`: estratégia, voz, calendário permanente, peças e revisão mensal, com referências de plataformas, formatos e calendário.

## 0.5.0 (13/10/2026)

- O plugin passou a funcionar no Codex a partir da mesma fonte.
- `novidade`, `diagnostico`, `plano-trimestral`, `ensinar` e `revisar` deixaram de ser comandos e viraram skills, porque o Codex não carrega comandos de plugin.
- As skills passaram a apontar para o protocolo por caminho relativo.
- A pasta de contexto ganhou uma busca que não depende da configuração do Claude Code: instruções do projeto, depois `~/.config/business-ops/context-folder`, depois o diretório atual.

## 0.4.0 (13/10/2026)

- O plugin foi renomeado de `negocio-coach` para `business-ops`, e o arquivo de perfil para `business-ops-contexto.md`.

## 0.3.1 e anteriores

- Versões iniciais, com o nome `negocio-coach`, só para Claude Code.
