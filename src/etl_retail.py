import pandas as pd

print("Chargement dataset Retail...")

df = pd.read_csv(
    "data/raw/online_retail.csv",
    encoding="latin1"
)

print("Nombre initial de lignes :", len(df))

df = df.drop_duplicates()

df = df.dropna(subset=["CustomerID"])

df = df[df["UnitPrice"] > 0]

df["InvoiceDate"] = pd.to_datetime(
    df["InvoiceDate"]
)

codes_to_remove = [
    "POST",
    "D",
    "C2",
    "M",
    "BANK CHARGES"
]

df = df[
    ~df["StockCode"].isin(codes_to_remove)
]

print("Nombre final de lignes :", len(df))

df.to_csv(
    "data/silver/retail_clean.csv",
    index=False
)

print("ETL Retail terminé")