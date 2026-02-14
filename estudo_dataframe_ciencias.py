import pandas as pd

lista_nomes = ['Anthony','Andri','Euclides','Vitor','Patrick','Carlos','Pedro']
print('Lista de nomes: \n',lista_nomes)
print('Primeiro elemento da lista 0> ', lista_nomes[0])

dicionario_pessoa = {
    'nome': 'Andri',
    'idade': 25,
    'cidade': 'Santa Maria',
}

print('Dicionario de uma pessoa : \n',dicionario_pessoa)
print("Atributo do Dicionario: \n",dicionario_pessoa.get('nome'))

#lista de dicionario
dados = [
    {'nome': 'Andri','idade': 25, 'cidade': 'Santa Maria',},
    {'nome': 'Anthony', 'idade': 23, 'cidade': 'São Pedro do Sul'}
]

#DataFrame: estrutura de dados bidimensional
df = pd.DataFrame(dados)
print('DataFrame: \n',df)

print(type(df))

# mostra coluna
print(df['nome'])

# mostra várias colunas
print(df[['idade','nome','cidade']])

# seleciona por índica
print('Primeira linha: \n',df.iloc[0])

# adiciona nova coluna
df['salario'] = [4100, 3200]

print(df['salario'])

# adiciona novo registro
df.loc[len(df)] = {
    'nome': 'Cleiton',
    'idade': 20,
    'cidade': 'Taubáte',
    'salario': 4200
}

print("\nelemento 0 -> \n")
print(df.iloc[0])

print("elemento 1 -> \n")
print(df.iloc[1])

print("\nelemento 2 -> \n")
print(df.iloc[2])

print('\n DataFrame Atual \n', df)

# remover uma coluna
df.drop('salario', axis=1, inplace=True)

# filtrando pessoas com mais de 29 anos
filtro_idade = df[df['idade'] >= 21]
print('Filtro por idade -> ',filtro_idade)

# salvando o dataframe em um arquivo CSV
df.to_csv('dados.csv', index=False)

# Lendo um arquivo CSV em um DataFrame
df_lido = pd.read_csv('dados.csv')
print('\n leitura do CSV \n',df_lido)