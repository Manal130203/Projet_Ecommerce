import pandas as pd

print("Chargement dataset Shipping...")

df = pd.read_csv(
    "data/raw/Shipping.csv"
)

print("Nombre initial de lignes :", len(df))

df = df.drop_duplicates()

df = df.dropna()

print("Nombre final de lignes :", len(df))

df.to_csv(
    "data/silver/shipping_clean.csv",
    index=False
)

print("ETL Shipping terminé")