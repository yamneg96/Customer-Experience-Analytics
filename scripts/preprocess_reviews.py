# scripts/preprocess_reviews.py
import pandas as pd

df = pd.read_csv("data/bank_reviews_raw.csv")

# Drop duplicates
df.drop_duplicates(subset=["review", "date", "bank"], inplace=True)

# Drop missing data
df.dropna(subset=["review", "rating", "date", "bank"], inplace=True)

# Standardize date
df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')

# Select required columns
df = df[["review", "rating", "date", "bank", "source"]]

df.to_csv("data/bank_reviews_clean.csv", index=False)
print("Cleaned data saved to data/bank_reviews_clean.csv")
