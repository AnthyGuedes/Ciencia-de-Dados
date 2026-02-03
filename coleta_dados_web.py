import requests
from bs4 import BeautifulSoup

url = 'https://python.org.br/'
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text, 'html.parser')

#print(extracao.text.strip())

"""
# FILTRO POR TAG ]
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