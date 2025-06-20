# scripts/scrape_reviews.py
from google_play_scraper import reviews_all
import pandas as pd

apps = {
    "CBE": "com.cbe.mobile.android",
    "BOA": "com.boa.app",       # Replace with actual package name
    "Dashen": "com.dashen.app"  # Replace with actual package name
}

all_reviews = []

for bank, package in apps.items():
    print(f"Scraping reviews for {bank}...")
    reviews = reviews_all(
        package,
        lang='en',
        country='us',
        sleep_milliseconds=0,
    )
    for r in reviews:
        all_reviews.append({
            "review": r['content'],
            "rating": r['score'],
            "date": r['at'].strftime('%Y-%m-%d'),
            "bank": bank,
            "source": "Google Play"
        })

df = pd.DataFrame(all_reviews)
df.to_csv("data/bank_reviews_raw.csv", index=False)
print("Raw review data saved to data/bank_reviews_raw.csv")
# scripts/scrape_reviews.py
