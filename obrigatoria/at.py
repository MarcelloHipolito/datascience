import pandas as pd
import numpy as np

# 1. Carregar o arquivo e inspecionar os dados
df = pd.read_csv('data.csv')
print("Dados originais:")
print(df)
print("\nInformações do DataFrame:")
print(df.info())

# 2. Substituir valores ausentes
# Identificando valores NA (no arquivo fornecido já estão como NA)
df.replace('NA', np.nan, inplace=True)

# Convertendo colunas numéricas para float
df['Vendas'] = df['Vendas'].astype(float)
df['Despesas'] = df['Despesas'].astype(float)

# Substituindo NA em Vendas pela mediana e Despesas pela média
median_vendas = df['Vendas'].median()
mean_despesas = df['Despesas'].mean()

df['Vendas'].fillna(median_vendas, inplace=True)
df['Despesas'].fillna(mean_despesas, inplace=True)

print("\nDados após substituição:")
print(df)

# 3. Agrupar por Região e Mês
grouped = df.groupby(['Região', 'Mês']).agg({
    'Vendas': 'sum',
    'Despesas': 'mean'
}).reset_index()

print("\nAgrupamento por Região e Mês:")
print(grouped)

# 4. Combinar horizontalmente Vendas e Despesas
combined = np.hstack((df[['Vendas']].values, df[['Despesas']].values))
print("\nCombinação horizontal de Vendas e Despesas:")
print(combined)

# 5. Sumário estatístico
summary = df.describe()
print("\nSumário estatístico:")
print(summary)