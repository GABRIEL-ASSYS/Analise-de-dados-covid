import pandas as pd

file_path = 'covid_19_clean_complete.csv'
df = pd.read_csv(file_path)

null_counts = df.isnull().sum()

dup_counts = df.apply(lambda col: col.duplicated().sum())

total_dup_rows = df.duplicated().sum()

print("🔍 Valores nulos por coluna:")
print(null_counts)

print("\n🔍 Valores duplicados por coluna:")
print(dup_counts)

print(f"\n🔍 Número total de linhas duplicadas no DataFrame: {total_dup_rows}")

if null_counts.any():
    print("\n⚠️ Existem colunas com valores nulos.")
else:
    print("\n✅ Não há valores nulos em nenhuma coluna.")

if dup_counts.any():
    print("⚠️ Existem valores duplicados em pelo menos uma coluna.")
else:
    print("✅ Não há valores duplicados dentro de nenhuma coluna.")

if total_dup_rows > 0:
    print("⚠️ Existem linhas duplicadas no DataFrame.")
else:
    print("✅ Não há linhas duplicadas no DataFrame.")