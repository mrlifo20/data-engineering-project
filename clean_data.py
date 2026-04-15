import pandas as pd


df = pd.read_csv("data/raw_sales.csv", encoding='latin1')

print(df.head())


print(df.info())

print(df.isnull().sum())


print("Duplicates:", df.duplicated().sum())
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')
df.columns = df.columns.str.strip()  # يشيل المسافات
df.columns = df.columns.str.replace(" ", "_")
# لو في Profit فاضي خليه 0
df['Profit'] = df['Profit'].fillna(0)

# لو في Sales فاضي احذفه (مهم)
df = df.dropna(subset=['Sales'])
df = df.drop_duplicates()
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
df['Profit'] = pd.to_numeric(df['Profit'], errors='coerce')
df.to_csv("data/cleaned_sales.csv", index=False)