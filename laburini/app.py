import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("estructura_ventas.csv")

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
avr = df["Monto_Total"].mean()
print(f"Promedio de Monto_Total: {avr}")
df["Monto_Total"] = df["Monto_Total"].fillna(avr)
print("Monto total actualizado:")
print(df["Monto_Total"])

print("\n--- INCONSISTENCIAS y FORMATO ---\n")
df["Región"] = df['Región'].str.title()
print("Valores estandarizados en la columna Región:")
print(df["Región"])
df["Unidades_Vendidas"] = pd.to_numeric(df["Unidades_Vendidas"])
print("Valores numericos estandarizados:")
print(df["Unidades_Vendidas"])

print("\n--- MEDIDAS DE TENDENCIA CENTRAL ---\n")
valor_medio = df["Monto_Total"].median()
valor_mas_comun = df["Monto_Total"].mode().item()
desviacion_estandar = df["Monto_Total"].std()

print(f"Valor medio: {valor_medio}")
print(f"Valor mas comun: {valor_mas_comun}")
print(f"Desviacion estandar: {desviacion_estandar}")

ventas_x_region = df.groupby("Región")["Monto_Total"].sum()
region_max = ventas_x_region.idxmax()
monto_max = ventas_x_region.max()

print("Region con mayor cantidad de monto total:")
print(f"Region: {region_max}")
print(f"Monto: {monto_max}")

producto_x_ventas = df.groupby("Producto")["Unidades_Vendidas"].sum()
producto_max = producto_x_ventas.idxmax()
ventas_max = producto_x_ventas.max()

print("Producto con mayor Unidades_Vendidas:")
print(f"Producto: {producto_max}")
print(f"Unidades_Vendidas: {ventas_max}")

x = df["Región"]
y = df["Monto_Total"]

plt.bar(x, y)
plt.show()

plt.hist(y)
plt.show()