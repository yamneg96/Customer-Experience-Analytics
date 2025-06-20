# 🏦 Ethiopian Banking App Reviews Analysis

This project analyzes mobile banking app reviews from the Google Play Store for three major Ethiopian banks:

- **Commercial Bank of Ethiopia (CBE)**
- **Bank of Abyssinia (BOA)**
- **Dashen Bank**

The objective is to extract user sentiment, identify themes, and uncover pain points to provide actionable insights to Omega Consultancy — a firm advising banks on customer satisfaction and retention.

## 📁 Project Structure

```bash
.
├── data/                   # Raw and cleaned datasets
├── notebooks/              # Jupyter notebooks
│   └── scrape_and_preprocess.ipynb
├── scripts/                # Reusable Python scripts
│   ├── scrape_reviews.py
│   └── preprocess_reviews.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ✅ Task 1: Data Collection and Preprocessing

### 🔍 Methodology

#### 1. Web Scraping

- Used the `google-play-scraper` Python library to scrape reviews for each bank’s app from the Google Play Store.
- Each review includes:
  - Review text
  - Rating (1–5 stars)
  - Date
  - Bank name
  - Source ("Google Play")
- Collected **400+ reviews per bank** for a total of **1,200+ reviews**.

#### 2. Saving Raw Data

- All reviews were saved into a combined CSV file:  
  `data/bank_reviews_raw.csv`
- Additionally, separate CSV files were created for each bank:
  - `data/reviews_cbe.csv`
  - `data/reviews_boa.csv`
  - `data/reviews_dashen.csv`

#### 3. Preprocessing

- Removed duplicates based on review text, date, and bank.
- Dropped rows with missing values in key fields.
- Normalized the date format to `YYYY-MM-DD`.
- Final cleaned dataset saved to:  
  `data/bank_reviews_clean.csv`

  ---

## 📊 Task 2: Sentiment and Thematic Analysis

### 🔍 Sentiment Analysis

- Applied `distilbert-base-uncased-finetuned-sst-2-english` to compute sentiment for over 1,200 reviews.
- Classified each review as **Positive**, **Negative**, or **Neutral** (based on label and score).
- Saved results to `data/sentiment_analysis.csv`.

### 💡 Thematic Analysis

- Extracted significant keywords and bigrams using TF-IDF (`sklearn`).
- Manually grouped keywords into 3–5 high-level themes per bank:
  - Account Access Issues
  - Transaction Performance
  - User Interface & Experience
  - Customer Support
  - Feature Requests
- Saved results to `data/keywords_and_themes.csv`.

### 📌 Key Deliverables

- Sentiment scores for 90%+ reviews
- Thematic keyword table with grouped categories
- Jupyter notebook with plots and insights
