# business-ops

Plugin para Claude Code e Codex que ajuda a tocar o trabalho de negócios de uma pequena empresa: vendas, pós-venda, marketing, redes sociais, processos, finanças e gestão. Ele trabalha a partir do contexto que você salva sobre as suas próprias empresas e explica o motivo de cada recomendação enquanto faz a tarefa.

O plugin ainda é um rascunho em uso pelo autor. O repositório é privado.

## Como funciona

No primeiro uso, a skill `contexto-negocio` conversa com você em blocos curtos e pergunta quem você é na empresa, o que ela vende, para quem, em que estágio está, qual é a principal dificuldade hoje e quanto você já conhece de cada área. As respostas ficam em arquivos Markdown numa pasta do seu computador, um arquivo de perfil e uma pasta por empresa.

Daí em diante, cada skill lê esse contexto antes de agir. Quem tem mais de uma empresa mantém uma pasta para cada, e o plugin não leva preço, cliente ou prática de uma para a outra.

Três regras valem para todas as skills:

- Material que vai para o cliente usa apenas o que está confirmado. Cada informação da empresa é marcada como confirmada, representada, planejada, hipótese ou desconhecida, e planos e preços vêm de um catálogo com status.
- O diagnóstico vem antes da recomendação, e a recomendação principal é uma só, com a primeira ação e o critério para saber se funcionou.
- Toda entrega traz o que fazer, o porquê, o erro comum e o próximo passo. Perguntas simples recebem resposta simples.

Enviar mensagem, publicar, gastar dinheiro ou assumir compromisso em seu nome depende do seu aval para aquela ação. O plugin entrega o texto pronto e você envia.

## Skills

| Skill | Para quê |
| --- | --- |
| `contexto-negocio` | Criar e manter o perfil e o contexto de cada empresa |
| `vendas` | Responder leads, preparar conversas, demonstrações, propostas e follow-up, lidar com objeção de preço |
| `vendas-saas` | Organizar funil e métricas de receita recorrente e avaliar se é hora de escalar |
| `sucesso-cliente` | Implantação, ativação, acompanhamento, cancelamento, renovação e indicação |
| `pesquisa-mercado` | Entrevistas com clientes, validação de público e oferta, concorrentes |
| `marca-oferta` | Posicionamento, proposta de valor, planos, preço e tom de voz |
| `propostas-apresentacoes` | Propostas, apresentações e folhas de planos a partir dos modelos da empresa |
| `marketing` | Escolha de canais, plano de marketing e experimentos |
| `social-media` | Estratégia, pilares, calendário permanente e peças para redes sociais |
| `anuncios` | Campanhas pagas, textos de anúncio e leitura de resultados |
| `influencia` | Criadores, afiliados e parcerias |
| `video-motion` | Vídeos em motion, do roteiro ao MP4 |
| `processos-documentacao` | Procedimentos, checklists, políticas e manuais |
| `sistemas` | Escolha e especificação de CRM, planilhas e automações |
| `gestao-estrategia` | Prioridades, metas, planos e rotina de gestão |
| `financas` | Caixa, margem, preço, ponto de equilíbrio e custo por cliente |
| `novidade` | Registrar um lançamento ou mudança de preço e listar o que precisa ser atualizado |
| `diagnostico` | Avaliar uma área da empresa e apontar as três prioridades |
| `plano-trimestral` | Plano de 90 dias com metas, tarefas por semana e revisão |
| `ensinar` | Explicar um conceito usando a sua empresa como exemplo |
| `revisar` | Criticar um material e reescrever os trechos fracos |

As skills são acionadas pelo próprio pedido. Também dá para chamá-las pelo nome: `/business-ops:vendas` no Claude Code, `$vendas` no Codex.

## Instalação

O repositório é privado, então a instalação exige acesso a ele.

Claude Code:

```
claude plugin marketplace add pv-ca/business-ops
claude plugin install business-ops@pvca
```

Codex:

```
codex plugin marketplace add pv-ca/business-ops
codex plugin add business-ops@pvca
```

Depois de instalar, abra uma sessão nova.

## Pasta de contexto

O plugin precisa saber onde ficam os arquivos das suas empresas. Ele procura nesta ordem:

1. A pasta configurada no plugin, que só existe no Claude Code:

   ```
   claude plugin configure business-ops@pvca
   ```

2. A pasta indicada nas instruções do projeto em que você está trabalhando, por exemplo num `AGENTS.md`.
3. O caminho escrito em `~/.config/business-ops/context-folder`, uma linha com o caminho absoluto. É o que faz o plugin funcionar no Codex a partir de qualquer diretório.
4. O diretório atual.

A pasta fica assim:

```
<pasta de contexto>/
  business-ops-contexto.md            perfil e índice das empresas
  <empresa>/contexto.md               identidade, posicionamento, o que está confirmado
  <empresa>/catalogo.md               planos, preços e recursos, cada um com status
  <empresa>/novidades.md              histórico de lançamentos e mudanças
  <empresa>/adaptacao-dos-metodos.md  como os métodos gerais se aplicam a esta empresa
  <empresa>/modelos/                  modelos de proposta, apresentação e mensagem
  <empresa>/processos/                procedimentos, políticas e manuais
  <empresa>/social/                   estratégia, voz e calendário de redes sociais
  <empresa>/entregas/                 rascunhos, uma pasta por pedido
  marca/<empresa>/identidade.md       cores, tipografia, uso do logo e tom
```

Os arquivos são criados quando a empresa precisa deles pela primeira vez.

## O que funciona em cada agente

| Recurso | Claude Code | Codex |
| --- | --- | --- |
| Skills | Sim | Sim |
| Atalhos `/business-ops:contexto`, `proposta`, `apresentacao` e `processo` | Sim | Não; chame a skill correspondente |
| Pasta de contexto configurada no plugin | Sim | Não; use `~/.config/business-ops/context-folder` |

O plugin não tem hooks, servidores MCP nem scripts. Ele é feito só de instruções em Markdown.

## Privacidade

O contexto das suas empresas fica na sua pasta, no seu computador. O plugin não contém dado de nenhuma empresa e não envia nada para fora por conta própria. O que você conversa com o agente segue as regras do Claude Code ou do Codex.

As skills pedem que dados pessoais de clientes fiquem na biblioteca de documentos da empresa e não sejam copiados para a pasta de contexto.

## Plugins que combinam

- `hyperframes`, da HeyGen: a skill `video-motion` planeja o vídeo e usa esse plugin para animar e renderizar.
- `marketing-skills`, de Corey Haines: quando está instalado, as skills de marketing e de redes sociais passam a ele a execução detalhada.

Nenhum dos dois é obrigatório.

## Métodos e livros

Quatro skills trazem um playbook próprio em `references/`: vendas, receita recorrente, sucesso do cliente e pesquisa com clientes. As demais têm um arquivo `references/books.md` que indica o livro de onde vem cada método.

A base de conhecimento dos livros ainda está em preparação. Os arquivos trazem resumos escritos com palavras próprias, sem trechos copiados, e as skills mandam buscar na web o que muda rápido: regras de plataformas de anúncio e de redes sociais, preços de mercado, leis e tributos.

O plugin não substitui contador, advogado nem outro profissional habilitado.

## Estrutura do repositório

```
.claude-plugin/marketplace.json   catálogo de onde o plugin é instalado
business-ops/                     o plugin
  .claude-plugin/plugin.json      manifesto e versão
  skills/<nome>/SKILL.md          uma pasta por skill, com suas referências
  commands/                       atalhos do Claude Code
  README.md                       notas técnicas, em inglês
CHANGELOG.md
```

Os arquivos de instrução das skills estão em inglês. As respostas saem no idioma de quem usa, português do Brasil por padrão.

## Licença

Ainda não definida. Enquanto o repositório for privado e não houver arquivo de licença, todos os direitos são reservados ao autor.
