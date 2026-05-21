import pandas as pd 

dados = {
    'Nome': ['João', 'Maria', 'Pedro', 'Ana'],
    'Idade': [25, 30, 35, 40],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']
}
df = pd.DataFrame(dados)

print(df)

# Metodo describe() para obter estatísticas descritivas
print(df.describe())

# Metodo info() para obter informações sobre o DataFrame
print(df.info())

#Para inserir uma nova coluna
df['Salário'] = [3000, 4000, 5000, 6000]
print(df)

#metodo del para deletar uma coluna
del df['Salário']

#metodo drop para deletar uma coluna
df = df.drop('Cidade', axis=1)
print(df)

#metodo para concatenar DataFrames
dados2 = {
    'Nome': ['Carlos', 'Daniela'],
    'Idade': [45, 35],
    'Cidade': ['Porto Alegre', 'Recife']
}
df2 = pd.DataFrame(dados2)
df_concatenado = pd.concat([df, df2], ignore_index=True)
print(df_concatenado)

#lindando com valores duplicados
dados3 = {
    'Nome': ['João', 'Maria', 'Pedro', 'Ana', 'João'],
    'Idade': [25, 30, 35, 40, 25],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'São Paulo']
}
df3 = pd.DataFrame(dados3)
print(df3)

# Remover valores duplicados
df3_sem_duplicados = df3.drop_duplicates()
print(df3_sem_duplicados)

#usando o metodo duplicated para identificar valores duplicados
duplicados = df3.duplicated()
print(duplicados)

#Ajustando o indice do DataFrame
df3_sem_duplicados.reset_index(drop=True, inplace=True)
print(df3_sem_duplicados)

#Usando o reset_index para ajustar o indice do DataFrame
df_concatenado.reset_index(drop=True, inplace=True)
print(df_concatenado)

# para evitar restribuição de indice, podemos usar o ignore_index=True no metodo concat
df_concatenado = pd.concat([df, df2], ignore_index=True)
print(df_concatenado)

#Como identificar e lidar com valores ausentes
dados4 = {
    'Nome': ['João', 'Maria', 'Pedro', 'Ana'],
    'Idade': [25, 30, None, 40],
    'Cidade': ['São Paulo', None, 'Belo Horizonte', 'Curitiba']
}

df4 = pd.DataFrame(dados4)
print(df4)

#Dropna os valores ausentes
df4_sem_ausentes = df4.dropna()

print(df4_sem_ausentes)

#Preenchendo os valores ausentes com um valor específico
df4_preenchido = df4.fillna('Desconecido')
print(df4_preenchido)

#Preenchendo valores ausentes com N/D
df4_preenchido_ND = df4.fillna('N/D')
print(df4_preenchido_ND)
