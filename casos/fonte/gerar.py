# -*- coding: utf-8 -*-
"""Gera as páginas casos/*.dc.html e o índice casos/index.html a partir dos arquivos casos/fonte/caso-*.md.

Uso (na raiz do repositório):  python casos/fonte/gerar.py

Formato dos .md: bloco inicial entre linhas "---" com chaves (numero, titulo, rotulo, subtitulo, resumo,
imagem, alt, credito); depois o corpo, com "## " e "### " para títulos, "| a | b |" para linhas de tabela
(a primeira linha é o cabeçalho), "- " para itens de lista ("  - " para subitens), "> " para a nota de
simulação, "!!! " para a caixa de atenção, "Fonte:" para a nota de fonte e linhas soltas para parágrafos.
Sem dependências além do Python 3."""
import os, re, html, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CASOS = os.path.join(RAIZ, 'casos')
FONTE = os.path.join(CASOS, 'fonte')
ARQUIVOS = {
    '7': 'Caso 7 - Alocacao de vagas em creches.dc.html',
    '29': 'Caso 29 - Fiscalizacao de transito por video.dc.html',
    '83': 'Caso 83 - Correcao automatizada de redacao.dc.html',
    '181': 'Caso 181 - Deteccao de furtos em espaco publico.dc.html',
    '186': 'Caso 186 - Previsao do nivel de rios.dc.html',
}

FB = "font-family:'Raleway',sans-serif;"
S = {
    'eyebrow': "margin:0 0 6pt;font-family:'rawline',sans-serif;font-size:9.5pt;font-weight:600;color:#1351b4;letter-spacing:.04em;",
    'h1': "margin:0 0 8pt;font-family:'rawline',sans-serif;font-size:24pt;font-weight:700;color:#0c326f;line-height:1.15;",
    'sub': "margin:0 0 14pt;" + FB + "font-size:11pt;color:#555555;line-height:1.4;",
    'fig': "margin:0 0 16pt;break-inside:avoid;",
    'img': "width:100%;height:auto;display:block;",
    'figcap': "margin:4pt 0 0;" + FB + "font-size:8.5pt;color:#767676;line-height:1.4;",
    'note': "margin:0 0 18pt;padding:10pt 12pt;background:#e8eefb;" + FB + "font-size:9.5pt;color:#555555;line-height:1.5;font-style:italic;break-inside:avoid;",
    'h2': "margin:22pt 0 8pt;font-family:'rawline',sans-serif;font-size:16pt;font-weight:700;color:#0c326f;",
    'h3': "margin:14pt 0 6pt;font-family:'rawline',sans-serif;font-size:12pt;font-weight:600;color:#1351b4;",
    'p': "margin:0 0 10pt;" + FB + "font-size:10.5pt;line-height:1.55;color:#333333;",
    'callout': "margin:0 0 10pt;padding:8pt 12pt;background:#fff9e0;" + FB + "font-size:10.5pt;line-height:1.55;color:#333333;break-inside:avoid;",
    'source': "margin:14pt 0 0;" + FB + "font-size:9pt;color:#767676;line-height:1.4;",
    'ul': "margin:0 0 10pt;padding-left:16pt;" + FB + "font-size:10.5pt;line-height:1.55;color:#333333;",
    'ul_in': "margin:4pt 0 0;padding-left:16pt;",
    'li': "margin-bottom:4pt;",
    'table': "width:100%;border-collapse:collapse;" + FB + "font-size:10pt;margin:0 0 12pt;",
    'th': "text-align:left;padding:6pt 8pt;background:#e8eefb;color:#0c326f;",
    'td': "padding:6pt 8pt;border-bottom:1px solid #e6e6e6;",
}
LARGURAS = {'Pergunta': ['38%'], 'Item': ['28%'], 'Parte interessada': ['34%'], 'Dano': ['26%', '24%'],
            'Tema': ['22%', '39%'], 'Medida': ['48%', '30%']}

def inline(t):
    t = html.escape(t.strip(), quote=False)
    return re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)

def ler(caminho):
    linhas = open(caminho, encoding='utf-8').read().splitlines()
    assert linhas[0].strip() == '---', caminho
    fim = linhas.index('---', 1)
    meta = {}
    for l in linhas[1:fim]:
        k, _, v = l.partition(':'); meta[k.strip()] = v.strip()
    return meta, linhas[fim + 1:]

def blocos(linhas):
    """Agrupa as linhas do corpo em blocos: (tipo, dados)."""
    out, par, tabela, lista = [], [], [], []
    def fecha():
        nonlocal par, tabela, lista
        if par: out.append(('p', ' '.join(par))); par = []
        if tabela: out.append(('table', tabela)); tabela = []
        if lista: out.append(('ul', lista)); lista = []
    for l in linhas:
        s = l.rstrip()
        if not s.strip(): fecha(); continue
        if s.startswith('## '): fecha(); out.append(('h2', s[3:])); continue
        if s.startswith('### '): fecha(); out.append(('h3', s[4:])); continue
        if s.startswith('> '): fecha(); out.append(('note', s[2:])); continue
        if s.startswith('!!! '): fecha(); out.append(('callout', s[4:])); continue
        if s.startswith('Fonte:'): fecha(); out.append(('source', s)); continue
        if s.startswith('|'):
            if par or lista: fecha()
            if re.match(r'^\|\s*-', s): continue
            tabela.append([c.strip() for c in s.strip().strip('|').split('|')]); continue
        if s.startswith('- ') or s.startswith('  - '):
            if par or tabela: fecha()
            nivel = 1 if s.startswith('  ') else 0
            lista.append((nivel, s.strip()[2:])); continue
        if tabela or lista: fecha()
        par.append(s.strip())
    fecha()
    return out

def tabela_html(linhas):
    cab = linhas[0]; larguras = LARGURAS.get(cab[0], [])
    ths = ''.join('<th style="%s%s">%s</th>' % (S['th'], ('width:%s;' % larguras[i]) if i < len(larguras) else '', inline(c)) for i, c in enumerate(cab))
    corpo = '\n'.join('    <tr>%s</tr>' % ''.join('<td style="%s">%s</td>' % (S['td'], inline(c)) for c in r) for r in linhas[1:])
    return '<table style="%s">\n  <thead><tr>%s</tr></thead>\n  <tbody>\n%s\n  </tbody>\n</table>\n' % (S['table'], ths, corpo)

def lista_html(itens):
    out = ['<ul style="%s">' % S['ul']]
    i = 0
    while i < len(itens):
        nivel, txt = itens[i]
        sub = []
        while i + 1 < len(itens) and itens[i + 1][0] > nivel:
            sub.append(itens[i + 1][1]); i += 1
        h = inline(txt)
        if sub:
            h += '\n    <ul style="%s">' % S['ul_in'] + ''.join('\n      <li style="%s">%s</li>' % (S['li'], inline(x)) for x in sub) + '\n    </ul>\n  '
        out.append('  <li style="%s">%s</li>' % (S['li'], h)); i += 1
    out.append('</ul>\n')
    return '\n'.join(out)

def pagina(meta, corpo, cabeca, cauda):
    out = ['<doc-page margin="0.75in">',
           '<div slot="footer" style="display:flex;justify-content:space-between;font-family:\'rawline\',sans-serif;font-size:8.5pt;color:#767676;border-top:1px solid #e6e6e6;padding-top:6pt;">',
           '  <span>Oficina AIE · Conexão SISP</span>', '  <span>%s</span>' % inline(meta['rotulo']), '</div>\n',
           '<p style="%s">Avaliação de impacto do sistema de IA</p>' % S['eyebrow'],
           '<h1 style="%s">%s</h1>' % (S['h1'], inline(meta['titulo'])),
           '<p style="%s">%s</p>' % (S['sub'], inline(meta['subtitulo']))]
    if meta.get('imagem'):
        out.append('<figure style="%s"><img src="%s" alt="%s" style="%s"><figcaption style="%s">%s</figcaption></figure>'
                   % (S['fig'], html.escape(meta['imagem']), html.escape(meta.get('alt', '')), S['img'], S['figcap'], inline(meta.get('credito', ''))))
    for tipo, dados in blocos(corpo):
        if tipo == 'note': out.append('<p style="%s">%s</p>\n' % (S['note'], inline(dados)))
        elif tipo == 'h2': out.append('<h2 style="%s%s">%s</h2>\n' % (S['h2'], 'break-before:page;' if dados.startswith('Avaliação de impacto') else '', inline(dados)))
        elif tipo == 'h3': out.append('<h3 style="%s">%s</h3>' % (S['h3'], inline(dados)))
        elif tipo == 'p': out.append('<p style="%s">%s</p>\n' % (S['p'], inline(dados)))
        elif tipo == 'callout': out.append('<p style="%s">%s</p>\n' % (S['callout'], inline(dados)))
        elif tipo == 'source': out.append('<p style="%s">%s</p>\n' % (S['source'], inline(dados)))
        elif tipo == 'table': out.append(tabela_html(dados))
        elif tipo == 'ul': out.append(lista_html(dados))
    return cabeca + '\n'.join(out) + '\n' + cauda

def indice(metas, modelo):
    itens = []
    for m in metas:
        href = ARQUIVOS[m['numero']].replace(' ', '%20')
        itens.append('    <li>\n      <a href="%s">%s</a>\n      <p>%s</p>\n    </li>' % (href, inline(m['rotulo'].replace(' · ', ' — ')), inline(m['resumo'])))
    ini = modelo.index('<ul class="casos">') + len('<ul class="casos">'); fim = modelo.index('</ul>', ini)
    return modelo[:ini] + '\n' + '\n'.join(itens) + '\n  ' + modelo[fim:]

def main():
    modelo = open(os.path.join(CASOS, ARQUIVOS['7']), encoding='utf-8').read()
    cabeca = modelo[:modelo.index('<doc-page')]; cauda = modelo[modelo.index('</doc-page>'):]
    metas = []
    for num, nome in ARQUIVOS.items():
        meta, corpo = ler(os.path.join(FONTE, 'caso-%s.md' % num))
        assert meta['numero'] == num
        with open(os.path.join(CASOS, nome), 'w', encoding='utf-8', newline='\n') as f:
            f.write(pagina(meta, corpo, cabeca, cauda))
        metas.append(meta); print('gerado', nome)
    idx = os.path.join(CASOS, 'index.html')
    modelo_idx = open(idx, encoding='utf-8').read()
    assert '<ul class="casos">' in modelo_idx, 'index.html sem a lista <ul class="casos">'
    with open(idx, 'w', encoding='utf-8', newline='\n') as f:
        f.write(indice(metas, modelo_idx))
    print('gerado index.html')

if __name__ == '__main__':
    main()
