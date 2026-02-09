import requests
from bs4 import BeautifulSoup

url = 'https://python.org.br/'
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text, 'html.parser')

#print(extracao.text.strip())

"""
# [ FILTRO POR TAG ]
for linha_texto in extracao.find_all('h1'):
    titulo = linha_texto.text.strip()
    print('titulo',titulo)
"""

## filtrando duas <tags> e contador para quantia de cada uma

contador_h2 = 0
contador_h1 = 0

for elemento in extracao.find_all(['h1','h2']):
    if elemento.name == 'h2':
        contador_h2 += 1
        titulo = elemento.text.strip()
        print('titulos h2 [ABAIXO]\n',titulo)


    elif elemento.name == 'h1':
        contador_h1 += 1
        texto = elemento.text.strip()
        print('titulos h1 [ABAIXO]\n',texto)

print('quantia de h2 = ', contador_h2)
print('quantia de h1 = ', contador_h1)

# TAGS ANINHADAS
print('TAGS ANINHADAS')
for elemento in extracao.find_all('h3'):
    # pegar a tag <a> esta dentro do h3 com nova versão do site
    link_titulo = elemento.find('a')
    url_link = link_titulo['href'] if link_titulo else 'sem link no título'

    print('\n titulo <h3> -> ', elemento.text.strip())
    print(' Link do Título <a> -> ', url_link)

    for link in elemento.find_next_siblings('p', limit=1): # next_siblings -> próximas após <h1> até achar <p>
        print(' Resumo <p> -> ', link.text.strip())

        for a in link.find_all('a', href=True):
            print('Texto Link (filho da aninhada) : ', a.text.strip(), ' | URL: ', a["href"])

# Alteração para que não aceite apenas <p> mas também  <div> ou <ul> como vizinhos do <h3>
print('\n --TAGS ANINHADAS-- |busca flexível| \n')
for elemento in extracao.find_all('h3'):
    print('Tituli <h3> {elemento.text.strip()}')

    vizinhos = elemento.find_next_siblings(['p', 'ul', 'div'], limit=1)

    for vizinho in vizinhos:

        print(f'  -> Vizinho encontrado  (Tag = <{vizinho.name}>):')

        # Mostra um pedaço do texto (primeiros 50 caracteres para não poluir)
        texto_limpo = vizinho.text.strip().replace('\n','')
        print(f'  Texto: "{texto_limpo[50]}..."')

        links = vizinho.find_all('a', href=True)

        if links:
            for link in links:
                print(f' [LINK]: {link.text.strip()} | URL: {link["href"]}')
        else:
            print("Nenhum link nesse bloco")
