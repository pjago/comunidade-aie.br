# Página da Imersão Ética em IA do Núcleo de IA

Página informativa da Imersão Ética em IA do Núcleo de Inteligência
Artificial (NIA), conduzida pela SGD/MGI, por meio da DEDIA, com apoio do CPQD no âmbito do
projeto INSPIRE.

O conteúdo vem do plano da imersão (`plano.md`, no repositório de trabalho da equipe).
Sempre que o plano mudar, esta página precisa acompanhar.

> **Nomes anteriores.** Até agosto de 2026 a ação se chamava "1ª Edição da Comunidade de
> Práticas Éticas do Núcleo de IA do Governo Federal". De agosto a setembro de 2026 chamou-se
> "1ª edição da Mentoria para Governança Ética do NIA". Desde setembro de 2026 o nome é
> **Imersão Ética em IA do Núcleo de IA**, sem numeração de edição. A pasta e a URL mantêm o
> nome antigo (`comunidade-aie.br`) de propósito — renomear quebraria os links dos casos já
> publicados em `casos/`.

## Duas saídas do mesmo conteúdo

As duas saídas não têm mais a mesma estrutura. O `index.html` é a **versão longa e autônoma**,
publicada no GitHub Pages. No Plone, o conteúdo se divide em duas peças: uma **página curta no
padrão gov.br** e um **edital simplificado em PDF**, publicado como Arquivo no Plone e linkado
da página. A paridade que se mantém é de conteúdo: **página curta + edital = página longa**.

| Arquivo | Onde é publicado | Como é feito |
|---|---|---|
| `index.html` | GitHub Pages, a partir da branch `main` | Versão longa autônoma: site estático de um arquivo, com HTML e CSS juntos |
| `imersao-etica-ia-plone.md` | Página curta no portal de IA do gov.br | Guia de montagem: um bloco de HTML por seção, com **estilo inline e classes do tema**, sem `<style>`, sem JavaScript e sem media query |
| `../Edital_Simplificado_Imersao_Etica_IA.md` | PDF publicado como Arquivo no Plone e linkado da página curta | Fonte em Markdown, convertida para `.docx` e então para PDF |

O guia `imersao-etica-ia-plone.md` substitui o antigo `mentoria-nia-plone.md`. As saídas
precisam ser atualizadas juntas. A página Plone não é conversão automática do `index.html`: o
filtro de sanitização remove o bloco `<style>`, as variáveis CSS, as media queries e o SVG
embutido em `data:`. E não se cola um arquivo só — a página se monta em blocos, colados um a um
no campo de texto rico. Por isso o artefato é um **guia de montagem**, com o HTML pronto de
cada bloco, as adaptações em relação à página autônoma e o checklist de publicação.

## Como editar

Abra o `index.html` e edite o texto direto. A tabela de seções abaixo vale para o
`index.html` — a página Plone curta tem estrutura própria, documentada no guia
`imersao-etica-ia-plone.md`. As seções seguem o percurso do participante —
**conhecer → escolher → participar → concluir e certificar** — a pedido da equipe de design, que
apontou que a versão anterior era "ler informações → ler informações → se inscrever":

| Seção | O que traz |
|---|---|
| Barra de identificação | Órgãos condutores |
| Hero | Nome da imersão, o que a equipe leva, e os quatro fatos principais |
| O que é a imersão | Objetivo e os três passos que cada equipe percorre |
| O Núcleo de Inteligência Artificial | O que é, o que faz, quem integra e como acionar |
| Duas formas de participar | Imersão (com inscrição) e encontros abertos (sem inscrição) |
| Como se inscrever | Vagas em destaque, composição da equipe, critérios e empates |
| Programação | Linha do tempo das cinco semanas, com marcador de formato |
| A oficina e as doze janelas | Regra de escolha da janela e a tabela J1–J12 |
| A reunião de relatório | Seção própria, a pedido da equipe de design |
| Três projetos na Semana Dados BR | Requisitos, autorização do órgão e regra de desempate |
| Certificados | Regra de presença e frequência mínima |
| Inscrições | Botões de chamada para ação |
| Rodapé | Condução, contexto e contato |

## Pendências marcadas no código

Procure por `TODO` no `index.html`:

1. **Link do formulário de inscrição**, no botão principal. Enquanto não existir, o botão fica
   com `aria-disabled="true"` e o rótulo "em breve".
2. **Link da transmissão** dos encontros abertos, no botão secundário. Depende da decisão entre
   Teams e YouTube.
3. **Endereço de contato**, no rodapé, a confirmar com a ASCOM. A equipe de design pediu
   explicitamente um `mailto:` no lugar de "contato a publicar" — o gabarito do link está no
   comentário, basta preencher o endereço.
4. **URL do PDF do edital no Plone** (`URL_DO_EDITAL`) — placeholder no guia
   `imersao-etica-ia-plone.md`, a preencher depois que o PDF do edital simplificado for
   publicado como Arquivo no Plone.

Ao preencher qualquer um deles, troque o `href="#"` pelo endereço real e remova o atributo
`aria-disabled`.

## Decisões de design já tomadas

Pontos em que os dois revisores divergiram e como ficou:

- **Ordem dos formatos** — a imersão vem primeiro, e não os encontros abertos. É o inverso da
  versão anterior: a imersão é o que exige decisão do leitor, e os encontros abertos não
  dependem de nada além do link.
- **Janelas da oficina** — na página longa (`index.html`) permanecem em tabela, e não em PDF
  para baixar: fazer o leitor baixar um arquivo para conferir um horário é atrito
  desnecessário. Na saída Plone, a decisão de setembro de 2026 prioriza a notícia curta no
  padrão gov.br — lá as janelas vivem no edital simplificado.
- **Linha do tempo** — sem ícones, para manter o layout simples, mas com dia da semana e horário
  padronizados em todos os itens, que era a inconsistência apontada.

## Antes de divulgar

A página é comunicação institucional publicada durante o período de defeso eleitoral. Seguindo
a orientação da CONJUR, as peças são **estritamente informativas e de orientação, limitadas às
informações necessárias à inscrição, participação e realização** da imersão — sem divulgação de
resultados ou realizações, sem nomes de autoridades e sem qualquer elemento de enaltecimento ou
promoção pessoal. Ainda assim, a peça precisa passar pela leitura da ASCOM antes de ir ao ar.
