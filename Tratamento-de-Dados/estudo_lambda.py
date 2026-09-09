import pandas as pd

# função para calcular o cubo de um número

def eleva_cubo(x):
    return x ** 3


# expressão de lambda para calcular o cudo de um número

eleva_cubo_lambda = lambda x: x ** 3 

print(eleva_cubo(2))
print(eleva_cubo_lambda(2))

df = pd.DataFrame({'números':[1,2,3,4,5,10]})

print('\nDataframe original: ')
print(df)

df['cubo_funcao'] = df['números'].apply(eleva_cubo)
df['cubo_lambda'] = df['números'].apply(lambda x: x ** 3)

print('\nDataframe com cubos: ')
print(df)

# operções complexas utilize funções(futuras atualização de código), para operações simples, utilize lambda