from transformers import pipeline
import pandas as pd

df = pd.read_csv("data/bank_reviews_clean.csv")

# Load sentiment model
sentiment_model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Predict sentiment
df["sentiment"] = df["review"].apply(lambda x: sentiment_model(x[:512])[0]['label'])
df["sentiment_score"] = df["review"].apply(lambda x: sentiment_model(x[:512])[0]['score'])

df.to_csv("data/sentiment_analysis.csv", index=False)
print("Sentiment analysis complete.")
