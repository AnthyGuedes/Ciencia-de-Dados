#https://brasilindicadores.com.br/pib/
import requests
from bs4 import BeautifulSoup
import pandas


print('Request:')
# faz requisição HTTP para o server e trás o código HTML bruto
response = requests.get('https://brasilindicadores.com.br/pib/')
print(response.text[:600])

print('BeautifulSoup:')
# analisa (faz parse) do HTML, cri a estrutura navegável/apresentável
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify()[:600])

print('Pandas:')
# procura especificamente pelas tags <table> do HTML e converte diretamente para o DataFrame(estrutura de dados)
url_dados = pandas.read_html('https://brasilindicadores.com.br/pib/')
#pega table
print(url_dados[0].head(10)) #head mostra topo, primeiras linhas definidas (da table)