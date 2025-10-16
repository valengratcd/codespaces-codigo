import pandas as pd

df = pd.read_csv("top_100_movies_full_best_effort.csv")

print("--- INSPECCION RAPIDA ---\n")
print(f"Filas (observaciones): {df.shape[0]}")
print(f"Columnas (variables): {df.shape[1]}")

print("\nTipo de datos (por columna):")
print(df.dtypes)

print("\nPrimeras 5 filas:")
print(df.head(5))

print("\n--- VALORES FALTANTES ---\n")
print("Valores faltantes:")
print(df.isna().sum())

print("\n")
print(df.nlargest(10, "Box Office ($M)"))