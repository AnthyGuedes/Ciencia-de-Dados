import pandas as pd

df = pd.read_csv(r"C:\EBAC_Ciencia_Dados_Repo\Ciencia-de-Dados\Tratamento-de-Dados\clientes.csv")


# o head() serve para mostrar apenas as 5 primeiras linhas do DataFrame. (Pode mudar o número de linhas)
print(df.head().to_string())
# para salvar em arquivo .txt
# df.head().to_string().to_csv("clientes_tratados.txt", index=False)

#Mostra os dados na ordem inversa em que foram inseridos
print(df.tail().to_string())

# mostra a quantidade de linhas e colunas
print('Qtd: ', df.shape)

# verifica tipos de dados do DataFrame
print('tipagem:\n ', df.dtypes)

# verifica valores nulos
print('valores nulos:\n', df.isnull().sum())