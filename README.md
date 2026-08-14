# Página do evento — 1ª Edição da Comunidade de Práticas Éticas

Página informativa da 1ª Edição da Comunidade de Práticas Éticas do Núcleo de
Inteligência Artificial do Governo Federal, conduzida pela SGD/MGI, por meio da DEDIA,
e pelo CPQD, no âmbito do projeto INSPIRE.

O conteúdo vem do plano do evento (`plano.md`, no repositório de trabalho da equipe).
Sempre que o plano mudar, esta página precisa acompanhar.

## Como é publicada

Site estático de um arquivo só. `index.html` traz o HTML e o CSS, sem JavaScript e sem
dependências além da fonte Raleway, carregada do Google Fonts.

A publicação é pelo GitHub Pages, a partir da branch `main`, na raiz do repositório.

## Como editar

Abra o `index.html` e edite o texto direto. As seções estão na ordem em que aparecem:

| Seção | O que traz |
|---|---|
| Barra de identificação | Órgãos condutores |
| Hero | Nome do evento, subtítulo e os quatro fatos principais |
| O que é | Objetivo e o que o órgão leva do evento |
| Duas trilhas | Trilha aberta e trilha restrita, lado a lado |
| Programação | Linha do tempo das cinco semanas |
| Como participar | Prazos e critérios de seleção das vagas livres |
| Janelas da oficina | As doze janelas e as datas de entrega do relatório |
| Certificados | Regra de presença e frequência mínima |
| Inscrições | Botões de chamada para ação |
| Rodapé | Condução, contexto e contato |

## Pendências marcadas no código

Procure por `TODO` no `index.html`:

1. **Link do formulário de inscrição** da trilha restrita, no botão principal.
   Enquanto não existir, o botão fica com `aria-disabled="true"` e o rótulo "em breve".
2. **Link da transmissão** da trilha aberta, no botão secundário. Depende da decisão
   entre Teams e YouTube.
3. **Endereço de contato**, no rodapé, a confirmar com a ASCOM.

Ao preencher qualquer um deles, troque o `href="#"` pelo endereço real e remova o
atributo `aria-disabled`.

## Antes de divulgar

A página é comunicação institucional publicada durante o período de defeso eleitoral.
O texto foi escrito em linguagem informativa e técnica, sem nomes de autoridades, sem
menção a realizações de governo e sem qualquer elemento de promoção pessoal. Ainda
assim, a peça precisa passar pela leitura da ASCOM antes de ir ao ar.
