import pandas as pd

df = pd.read_csv(r"C:\EBAC_Ciencia_Dados_Repo\Ciencia-de-Dados\Tratamento-de-Dados\clientes.csv")

pd.set_option('display.width', None)
print(df.head())

# remover dados
df.drop('pais', axis=1, inplace=True) # coluna
df.drop(2, axis = 0, inplace=True) # linha
