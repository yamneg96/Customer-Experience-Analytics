import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("data/bank_reviews_clean.csv")

# TF-IDF for keyword extraction
vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words="english", max_features=100)
X = vectorizer.fit_transform(df["review"])

keywords = vectorizer.get_feature_names_out()

# Create dataframe of top keywords (manual labeling of themes)
keywords_df = pd.DataFrame(keywords, columns=["keyword"])

# Sample manual theme grouping (you can refine it further)
theme_map = {
    "login": "Account Access",
    "error": "Account Access",
    "slow": "Performance",
    "transfer": "Performance",
    "crash": "Reliability",
    "interface": "User Experience",
    "support": "Customer Service",
    "fingerprint": "Feature Request"
}

keywords_df["theme"] = keywords_df["keyword"].map(lambda x: next((v for k, v in theme_map.items() if k in x), "Other"))

keywords_df.to_csv("data/keywords_and_themes.csv", index=False)
print("Thematic keywords saved.")
