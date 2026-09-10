# Imersão Ética em IA do Núcleo de IA — montagem no Plone (portal de IA do gov.br)

Guia para publicar a página da imersão no portal de IA do gov.br. **Não se cola o
`index.html` inteiro.** A plataforma já entrega a moldura — `br-header`, `br-footer`,
breadcrumb, fontes, `core.min.css` e `core-init.min.js` — e o que você monta é só o **miolo**,
em blocos de HTML colados no campo de texto rico.

Este guia substitui o `mentoria-nia-plone.md` e muda a estratégia da página: em vez de
reproduzir a página longa, a notícia no Plone é uma **página curta**, no padrão de tamanho da
página "Nuvem Brasileira" do gov.br — apresentação, como funciona e inscrição. O detalhe
(critérios de seleção, janelas J1–J12, programação completa, Semana Dados BR, certificados)
vive no **edital simplificado**, publicado como **Arquivo (PDF)** no Plone e linkado do último
bloco. A paridade de conteúdo é: **página curta + edital = página longa** (`index.html`, que
segue no GitHub Pages).

## O que muda em relação ao `index.html`

O filtro de sanitização do Plone descarta o que a versão autônoma usa para se sustentar:

| No `index.html` | No Plone |
|---|---|
| Bloco `<style>` de ~160 linhas | Não sobrevive — **estilo inline + classes do tema** |
| Variáveis CSS (`var(--blue)`) | Valores literais (`#1351b4`) |
| `@media(min-width:820px)` | **`flex-wrap`** com `flex-basis` e `min-width` |
| SVG embutido em `data:` no hero | Removido — o hero vira texto sobre o tema |
| Fonte Raleway do Google Fonts | Fonte do tema (Rawline) |
| Âncoras `#conteudo` e `scroll-behavior` | Sem JS e sem âncora própria |

## Convenções (leia uma vez)

**CSS que já vem carregado.** Bootstrap "sunburst" (`d-flex`, `flex-wrap`,
`justify-content-center`, `text-center`, `p-3`, `mb-3`, `mr-2`, `align-items-start`),
componentes do Design System gov.br (`br-button primary`, `br-tag`, `callout`, `text-primary`)
e **Font Awesome** (`fa-solid fa-…`). Use classe quando existir; caia no inline só para o que o
tema não cobre.

**Onde o `style` inline sobrevive.** Em `div`, `span`, `strong`, `i`, `p`, `a`, `ul`,
`blockquote`, `table`, `details` e `summary`. **Não sobrevive em `<button>`** — o filtro remove.
Se precisar estilizar um botão, use classe ou estilize os `<span>` filhos.

**Sem JavaScript e sem media query.** A linha do tempo é estática; a responsividade vem de
`flex-wrap` + `flex-basis` + `min-width`. Cada grade de cards usa `min-width:220px` como
gatilho de colapso.

**Padrão de card, reutilizado em tudo:**

```
style="padding:14px 16px; background:#ffffff; box-shadow:3px 3px 12px 0 rgba(0,0,0,.25);"
```

O sublinhado amarelo no título (`border-bottom:2px solid yellow`) vai em **todos os títulos de
card** — é o padrão das páginas irmãs do NIA (Ficha de Sistema de IA, Framework AIE).

**Paleta (tokens do Design System).** Azul interativo `#1351b4` · azul-escuro (hover) `#0c326f` ·
sucesso `#168821` (fundo `#ebf7ed`, texto `#0d5b16`) · erro `#e52207` · atenção `#ffcd07`
(fundo `#fff9e0`, texto `#6b5200`) · tint de marca `#edf5ff` · cinza de fundo `#f8f8f8` ·
cinza de borda `#ccced4` (do tema). Não usar valores fora desta lista.

**Lições das homologações anteriores (não repetir os defeitos):**

- `text-primary` só no **ícone** do callout — no contêiner ele pinta o texto inteiro de azul.
- `<p>` dentro de faixa colorida leva `color:#ffffff !important` — o tema sobrepõe a cor.
- Fecho de página em `<div>`, nunca `<blockquote>` — o tema aplica itálico a citações.
- Tabela larga sempre dentro de `div` com `overflow-x:auto` e `min-width` na tabela.
- Números grandes em `<p>` com `font-size`, não em `<h2>` — senão entram no sumário automático.
- Botão: `style` nos `<a>` e `<span>`, nunca em `<button>`; `!important` nas cores por causa da
  especificidade do `br-button`.
- `<p>` internos de card com `margin:0` — sem isso a margem padrão domina o espaçamento.
- Último item da linha do tempo **sem conector**, senão a linha sobra pendurada.

**Antes de montar tudo, teste um bloco.** Cole o **TEXTO RICO 1**, salve, e confira se o card e
a sombra renderizaram. O filtro varia entre instâncias — se o inline não pegar nesse bloco, não
vai pegar nos outros, e aí o caminho é abrir chamado na DTIC.

---

## Mapa de blocos

A página tem **seis tiles**: os títulos de seção ("Como funciona" e "Inscrições") são tiles
**Cabeçalho** próprios, e não `<h2>` dentro do texto rico — o tema já centraliza e dimensiona.

| # | Tile | Conteúdo |
|---|---|---|
| 1 | **CABEÇALHO 0** | Título da notícia |
| 2 | **TEXTO RICO 1** | Chips de datas + 3 cards: O que é · Público-alvo · Objetivos |
| 3 | **CABEÇALHO 1** | "Como funciona" |
| 4 | **TEXTO RICO 2** | Linha do tempo das cinco semanas |
| 5 | **CABEÇALHO 2** | "Inscrições" |
| 6 | **TEXTO RICO 3** | Datas, botões e link do edital |

O que **saiu da página** e agora está no edital: tabela de critérios (7 pontos), empates e
suplência, janelas J1–J12 com a reunião de relatório, requisitos da Semana Dados BR,
certificados e o detalhamento do NIA. A página aponta para o edital no TEXTO RICO 3.

---

## CABEÇALHO 0 — título

Título da notícia, sem HTML:

```
Imersão Ética em IA do Núcleo de IA
```

---

## TEXTO RICO 1 — O que é, público-alvo e objetivo

```html
<div class="d-flex flex-wrap mb-3" style="gap:8px;">
  <span class="br-tag" style="background:#edf5ff; color:#1351b4; padding:4px 12px; border-radius:999px; font-weight:600;">Inscrições de 16 a 30/09</span>
  <span class="br-tag" style="background:#edf5ff; color:#1351b4; padding:4px 12px; border-radius:999px; font-weight:600;">Imersão de 05/10 a 04/11 de 2026</span>
  <span class="br-tag" style="background:#edf5ff; color:#1351b4; padding:4px 12px; border-radius:999px; font-weight:600;">Totalmente on-line</span>
  <span class="br-tag" style="background:#edf5ff; color:#1351b4; padding:4px 12px; border-radius:999px; font-weight:600;">12 equipes selecionadas</span>
</div>

<p style="font-size:1.05em;">A Imersão Ética em IA acompanha equipes de órgãos públicos na avaliação de um sistema de inteligência artificial que elas mesmas desenvolvem ou operam. Não é só treinamento: é acompanhamento sobre um projeto seu, com começo, meio e fim marcados no calendário.</p>

<div class="d-flex flex-wrap" style="gap:16px; margin:16px 0 20px;">
  <div style="flex:1 1 30%; min-width:220px; padding:14px 16px; background:#ffffff; box-shadow:3px 3px 12px 0 rgba(0,0,0,.25);">
    <p style="margin:0 0 6px;"><i class="fa-solid fa-file-lines" style="color:#1351b4;"></i>
      <strong style="font-size:20px; border-bottom:2px solid yellow;">O que é</strong></p>
    <p style="margin:0;">Um ciclo de cinco semanas em que a equipe descreve o seu sistema na Ficha de Sistema de IA e avalia esse mesmo sistema com a Autoavaliação de Impacto Ético (AIE).</p>
  </div>
  <div style="flex:1 1 30%; min-width:220px; padding:14px 16px; background:#ffffff; box-shadow:3px 3px 12px 0 rgba(0,0,0,.25);">
    <p style="margin:0 0 6px;"><i class="fa-solid fa-users" style="color:#1351b4;"></i>
      <strong style="font-size:20px; border-bottom:2px solid yellow;">Público-alvo</strong></p>
    <p style="margin:0;">Equipes de 2 a 3 pessoas, de órgãos públicos federais, com um sistema de IA em produção ou em desenvolvimento. Com participação de até 2 equipes por órgão.</p>
  </div>
  <div style="flex:1 1 30%; min-width:220px; padding:14px 16px; background:#ffffff; box-shadow:3px 3px 12px 0 rgba(0,0,0,.25);">
    <p style="margin:0 0 6px;"><i class="fa-solid fa-list-check" style="color:#1351b4;"></i>
      <strong style="font-size:20px; border-bottom:2px solid yellow;">Objetivos</strong></p>
    <p style="margin:0;">Observar questões éticas no desenvolvimento de sistemas de IA para serviços públicos. Registrar a finalidade, a lógica de processamento e os limites técnicos. Classificar o risco ético e receber recomendações do que melhorar.</p>
  </div>
</div>

<div class="callout d-flex align-items-start mb-3">
  <span class="mr-2 text-primary"><i class="fa-solid fa-link"></i></span>
  <span>A imersão é conduzida pelo Núcleo de Inteligência Artificial (NIA) da Secretaria de Governo Digital. Os dois instrumentos usados estão publicados:
    <a href="https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/inteligencia-artificial-1/publicacoes/ficha-de-sistema-de-ia"><strong>Ficha de Sistema de IA</strong></a> e
    <a href="https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/inteligencia-artificial-1/publicacoes/framework-aie"><strong>Framework de Autoavaliação de Impacto Ético</strong></a>.</span>
</div>
```

> **Notas.** Os três cards seguem o padrão da página Nuvem Brasileira ("O que é · Público-Alvo
> · Objetivo") no dialeto visual da família NIA: sombra deslocada e sublinhado amarelo de 2px
> nos títulos. Ícones distintos por card. `min-width:220px` é o gatilho: abaixo disso os três
> cards viram um por linha.

---

## CABEÇALHO 1 — Como funciona

Tile **Cabeçalho**, texto puro, sem HTML:

```
Como funciona
```

---

## TEXTO RICO 2 — Como funciona

```html
<p>Cinco semanas, de 5 de outubro a 4 de novembro de 2026, totalmente on-line, com carga de até 3 horas por semana.</p>

<div style="padding:20px 22px; background:#ffffff; box-shadow:3px 3px 12px 0 rgba(0,0,0,.25); margin-top:16px;">
  <div style="width:fit-content; margin:0 auto;">

    <div style="display:flex; gap:14px;">
      <div style="display:flex; flex-direction:column; align-items:center;">
        <div style="flex-shrink:0; width:14px; height:14px; border-radius:50%; background:#1351b4; margin-top:6px;"></div>
        <div style="width:2px; height:100%; min-height:34px; background:#d4e5ff;"></div>
      </div>
      <div style="padding-bottom:18px;">
        <p style="margin:0; font-size:13px; font-weight:600; color:#1351b4;">5 de outubro &middot; 14h00</p>
        <p style="margin:0;"><strong>Aula inaugural — 1h30</strong>
          <span style="background:#edf5ff; color:#1351b4; font-size:12px; font-weight:600; padding:2px 8px; border-radius:999px;">Aberto</span></p>
        <p style="margin:0; font-size:15px; color:#555555;">Como se dará a imersão e apresentação da Ficha de Sistema de IA e da AIE.</p>
      </div>
    </div>

    <div style="display:flex; gap:14px;">
      <div style="display:flex; flex-direction:column; align-items:center;">
        <div style="flex-shrink:0; width:14px; height:14px; border-radius:50%; background:#168821; margin-top:6px;"></div>
        <div style="width:2px; height:100%; min-height:34px; background:#d4e5ff;"></div>
      </div>
      <div style="padding-bottom:18px;">
        <p style="margin:0; font-size:13px; font-weight:600; color:#1351b4;">5 a 16 de outubro &middot; assíncrono</p>
        <p style="margin:0;"><strong>Estudo dirigido — 2 semanas</strong>
          <span style="background:#ebf7ed; color:#0d5b16; font-size:12px; font-weight:600; padding:2px 8px; border-radius:999px;">Imersão</span></p>
        <p style="margin:0; font-size:15px; color:#555555;">Leitura do material de apoio e preenchimento da Ficha para o sistema da equipe, com canal aberto para dúvidas.</p>
      </div>
    </div>

    <div style="display:flex; gap:14px;">
      <div style="display:flex; flex-direction:column; align-items:center;">
        <div style="flex-shrink:0; width:14px; height:14px; border-radius:50%; background:#1351b4; margin-top:6px;"></div>
        <div style="width:2px; height:100%; min-height:34px; background:#d4e5ff;"></div>
      </div>
      <div style="padding-bottom:18px;">
        <p style="margin:0; font-size:13px; font-weight:600; color:#1351b4;">13 de outubro &middot; 14h00</p>
        <p style="margin:0;"><strong>Palestras com especialistas convidados — 3h</strong>
          <span style="background:#edf5ff; color:#1351b4; font-size:12px; font-weight:600; padding:2px 8px; border-radius:999px;">Aberto</span></p>
        <p style="margin:0; font-size:15px; color:#555555;">Especialistas apresentam conceitos de governança de IA e discutem estruturas, ferramentas e formas de mitigar riscos éticos.</p>
      </div>
    </div>

    <div style="display:flex; gap:14px;">
      <div style="display:flex; flex-direction:column; align-items:center;">
        <div style="flex-shrink:0; width:14px; height:14px; border-radius:50%; background:#168821; margin-top:6px;"></div>
        <div style="width:2px; height:100%; min-height:34px; background:#d4e5ff;"></div>
      </div>
      <div style="padding-bottom:18px;">
        <p style="margin:0; font-size:13px; font-weight:600; color:#1351b4;">20 a 27 de outubro &middot; 9h00 ou 14h00</p>
        <p style="margin:0;"><strong>Oficina de aplicação da AIE — 2h30</strong>
          <span style="background:#ebf7ed; color:#0d5b16; font-size:12px; font-weight:600; padding:2px 8px; border-radius:999px;">Imersão</span></p>
        <p style="margin:0; font-size:15px; color:#555555;">Cada equipe participa de uma das doze janelas, facilitada pelo Núcleo de IA.</p>
      </div>
    </div>

    <div style="display:flex; gap:14px;">
      <div style="display:flex; flex-direction:column; align-items:center;">
        <div style="flex-shrink:0; width:14px; height:14px; border-radius:50%; background:#168821; margin-top:6px;"></div>
        <div style="width:2px; height:100%; min-height:34px; background:#d4e5ff;"></div>
      </div>
      <div style="padding-bottom:18px;">
        <p style="margin:0; font-size:13px; font-weight:600; color:#1351b4;">23 a 30 de outubro &middot; 17h00 ou 17h30</p>
        <p style="margin:0;"><strong>Reunião de relatório — 30 min</strong>
          <span style="background:#ebf7ed; color:#0d5b16; font-size:12px; font-weight:600; padding:2px 8px; border-radius:999px;">Imersão</span></p>
        <p style="margin:0; font-size:15px; color:#555555;">Três dias úteis depois da oficina, para conversar sobre o resultado da avaliação.</p>
      </div>
    </div>

    <div style="display:flex; gap:14px;">
      <div style="display:flex; flex-direction:column; align-items:center;">
        <div style="flex-shrink:0; width:14px; height:14px; border-radius:50%; background:#1351b4; margin-top:6px;"></div>
      </div>
      <div>
        <p style="margin:0; font-size:13px; font-weight:600; color:#1351b4;">4 de novembro &middot; 14h00</p>
        <p style="margin:0;"><strong>Fechamento — 2h</strong>
          <span style="background:#edf5ff; color:#1351b4; font-size:12px; font-weight:600; padding:2px 8px; border-radius:999px;">Aberto</span></p>
        <p style="margin:0; font-size:15px; color:#555555;">Espaço para as equipes que quiserem compartilhar o seu sistema de IA e as suas considerações éticas.</p>
      </div>
    </div>

  </div>
</div>

<div class="callout d-flex align-items-start mb-3" style="margin-top:16px;">
  <span class="mr-2 text-primary"><i class="fa-solid fa-circle-info"></i></span>
  <span>Os encontros marcados como <strong>Aberto</strong> não têm inscrição: qualquer pessoa participa pelo link de transmissão publicado nesta página. As etapas marcadas como <strong>Imersão</strong> são exclusivas das 12 equipes selecionadas.</span>
</div>
```

> **Notas.** A linha do tempo é vertical — um stepper horizontal não é responsivo sem media
> query. O conector entre as bolinhas é um `div` de `width:2px` com `min-height:34px`; o
> **último item não tem conector**. A cor da bolinha distingue o formato: azul para encontro
> aberto, verde para etapa da imersão.

---

## CABEÇALHO 2 — Inscrições

Tile **Cabeçalho**, texto puro, sem HTML:

```
Inscrições
```

---

## TEXTO RICO 3 — Inscrições e edital

```html
<div style="background:#f8f8f8; border-radius:8px; padding:24px 20px; text-align:left;">
  <p>A inscrição é feita por formulário, de <strong>16 a 30 de setembro de 2026</strong>. Cada equipe inscreve um sistema de IA e o descreve no formulário. O resultado da seleção é divulgado em <strong>1º de outubro</strong>. Critérios de seleção e programação detalhada estão no edital.</p>
  <div class="py-3 d-flex flex-wrap justify-content-start" style="gap:12px;">
    <a class="br-button primary" style="display:inline-flex; align-items:center; gap:8px; padding:12px 28px; background-color:#1351b4 !important; border:none; border-radius:100em; text-decoration:none;" href="URL_DO_FORMULARIO">
      <i class="fa-solid fa-user-plus" style="color:#fff !important;">&nbsp;</i>
      <span style="color:#fff !important; font-weight:600;">Inscrever a minha equipe</span>
    </a>
    <a class="br-button" style="display:inline-flex; align-items:center; gap:8px; padding:12px 28px; border:2px solid #1351b4; border-radius:100em; text-decoration:none;" href="URL_DO_EDITAL">
      <i class="fa-solid fa-file-pdf" style="color:#1351b4 !important;">&nbsp;</i>
      <span style="color:#1351b4 !important; font-weight:600;">Edital (PDF)</span>
    </a>
    <a class="br-button" style="display:inline-flex; align-items:center; gap:8px; padding:12px 28px; border:2px solid #1351b4; border-radius:100em; text-decoration:none;" href="URL_DA_TRANSMISSAO">
      <i class="fa-solid fa-video" style="color:#1351b4 !important;">&nbsp;</i>
      <span style="color:#1351b4 !important; font-weight:600;">Link da transmissão</span>
    </a>
  </div>
  <p style="font-size:15px; color:#555555;">Dúvidas sobre a participação podem ser enviadas para cggia@gestao.gov.br.</p>
</div>
```

> **Notas.** Os três `href` são marcadores — `URL_DO_FORMULARIO`, `URL_DO_EDITAL` e
> `URL_DA_TRANSMISSAO` — e precisam ser trocados antes de publicar. Enquanto um deles não
> existir, **remova o `<a>` inteiro** em vez de deixá-lo apontando para lugar nenhum (o da
> transmissão só passa a existir perto de 05/10). O `style` está nos `<a>` e nos `<span>`,
> nunca em `<button>`; o `!important` é necessário pela especificidade do `br-button`. O fecho
> é `<div>`, e não `<blockquote>` — o tema aplica itálico a citações.

---

## O edital simplificado como Arquivo no Plone

O botão "Edital (PDF)" aponta para um **Arquivo** hospedado no próprio Plone:

1. Gere o PDF a partir de `artefatos/Edital_Simplificado_Imersao_Etica_IA.md` (via .docx).
2. No Plone, em **Adicionar item → Arquivo**, envie o PDF **antes** de montar o TEXTO RICO 3.
   Short name sem espaços e em minúsculas — ex.: `edital-simplificado-imersao-etica-em-ia.pdf`
   (espaço vira `%20` na URL).
3. **Publique o Arquivo** (o estado do anexo é independente do da página — anexo privado dá
   erro de acesso para o visitante).
4. Copie a URL final do Arquivo e cole no `href` do botão, no lugar de `URL_DO_EDITAL`.
5. Se o edital mudar depois, **substitua o conteúdo do mesmo Arquivo** (aba Edição → trocar o
   arquivo) em vez de criar outro — assim a URL não muda e o botão continua válido.

---

## Checklist de publicação

**Antes de montar**

- [ ] Colar **só o TEXTO RICO 1** e salvar. Conferir se o card, a sombra e o ícone renderizaram.
      Se o inline não sobreviver, pare: o caminho passa a ser chamado na DTIC.
- [ ] Subir e publicar o PDF do edital como Arquivo; anotar a URL.

**Conteúdo**

- [ ] Trocar `URL_DO_FORMULARIO`, `URL_DO_EDITAL` e `URL_DA_TRANSMISSAO` no TEXTO RICO 3 —
      removendo o `<a>` de qualquer um que ainda não exista.
- [ ] Recolar o TEXTO RICO 1 na página publicada: o card Público-alvo mudou para "de órgãos
      públicos federais" (sem "qualquer").
- [ ] Conferir as datas contra o `plano.md`: inscrições 16/09–30/09, resultado 01/10, aula
      inaugural 05/10, estudo 05–16/10, palestras 13/10, oficinas 20–27/10, relatórios
      23–30/10, fechamento 04/11.
- [ ] Conferir que as datas e regras citadas batem com o edital simplificado e com o
      formulário de inscrição.
- [ ] Nenhuma menção a "mentoria", "1ª edição", "AIE.BR", "Comunidade de Práticas Éticas",
      "trilha restrita" ou "SISP".

**Layout**

- [ ] Nenhum bloco causa rolagem horizontal na página inteira.
- [ ] Sublinhado amarelo nos títulos dos três cards do TEXTO RICO 1.
- [ ] Último item da linha do tempo sem conector pendurado.
- [ ] Ícones distintos entre si na grade de cards.
- [ ] Bloco final de inscrições sem itálico e botão primário **azul** `#1351b4`.

**Depois de publicar**

- [ ] Conferir em desktop e no celular, com captura de tela dos dois.
- [ ] Testar os links da Ficha de Sistema de IA, do Framework AIE, do formulário e do PDF do
      edital (deslogado, para pegar anexo não publicado).
- [ ] Passar pela leitura da ASCOM: a peça é comunicação institucional em período de defeso
      eleitoral — estritamente informativa e de orientação, limitada às informações necessárias
      à inscrição, participação e realização.

**O que fica fora do alcance daqui**

Cabeçalho, rodapé, menu, fontes, CSS em arquivo e qualquer JavaScript são do tema e da
plataforma — pedido à DTIC, não edição de conteúdo. Se aparecer a necessidade de um componente
que só funcione com script, prefira reescrever o conteúdo para não precisar dele.
