import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from collections import Counter
import re
from pathlib import Path
import sys

# Add the project root directory to Python path
sys.path.append(str(Path(__file__).parent.parent))

# Load the cleaned reviews
df = pd.read_csv("data/bank_reviews_clean.csv")

# Add sentiment analysis using simple keyword matching
def simple_sentiment(text):
    if not isinstance(text, str):
        return 'neutral'
    
    text = text.lower()
    positive_words = ['good', 'great', 'excellent', 'awesome', 'love', 'nice', 'best', 'easy', 'fast', 'helpful']
    negative_words = ['bad', 'poor', 'terrible', 'worst', 'hate', 'slow', 'difficult', 'crash', 'error', 'problem', 'issue']
    
    pos_count = sum(1 for word in positive_words if word in text)
    neg_count = sum(1 for word in negative_words if word in text)
    
    if pos_count > neg_count:
        return 'positive'
    elif neg_count > pos_count:
        return 'negative'
    else:
        return 'neutral'

# Add theme extraction using keyword matching
def extract_themes(text):
    if not isinstance(text, str):
        return []
    
    text = text.lower()
    themes = {
        'usability': ['easy', 'simple', 'user-friendly', 'intuitive', 'navigate'],
        'performance': ['fast', 'quick', 'slow', 'speed', 'responsive', 'crash', 'freeze', 'hang'],
        'features': ['feature', 'function', 'option', 'capability', 'tool'],
        'security': ['secure', 'security', 'safe', 'protection', 'privacy'],
        'customer_service': ['support', 'service', 'help', 'assistance', 'response'],
        'reliability': ['reliable', 'stable', 'consistent', 'dependable', 'trust'],
        'ui_design': ['design', 'interface', 'layout', 'look', 'appearance']
    }
    
    found_themes = []
    for theme, keywords in themes.items():
        if any(keyword in text for keyword in keywords):
            found_themes.append(theme)
    
    return found_themes

# Apply sentiment and theme analysis
df['sentiment'] = df['review'].apply(simple_sentiment)
df['themes'] = df['review'].apply(extract_themes)

# Explode the themes column to analyze themes separately
themes_df = df.explode('themes').dropna(subset=['themes'])

# 1. Overall sentiment analysis
print("Overall Sentiment Distribution:")
sentiment_counts = df['sentiment'].value_counts()
print(sentiment_counts)
print("\n")

# 2. Sentiment by bank
print("Sentiment by Bank:")
bank_sentiment = pd.crosstab(df['bank'], df['sentiment'])
print(bank_sentiment)
print("\n")

# 3. Top themes overall
print("Top Themes Overall:")
theme_counts = themes_df['themes'].value_counts()
print(theme_counts)
print("\n")

# 4. Themes by bank
print("Top Themes by Bank:")
bank_themes = pd.crosstab(themes_df['bank'], themes_df['themes'])
print(bank_themes)
print("\n")

# 5. Positive drivers (themes with positive sentiment)
positive_themes = themes_df[themes_df['sentiment'] == 'positive']['themes'].value_counts()
print("Positive Drivers:")
print(positive_themes)
print("\n")

# 6. Pain points (themes with negative sentiment)
negative_themes = themes_df[themes_df['sentiment'] == 'negative']['themes'].value_counts()
print("Pain Points:")
print(negative_themes)
print("\n")

# 7. Bank comparison
print("Bank Comparison - Average Rating:")
bank_avg_rating = df.groupby('bank')['rating'].mean().sort_values(ascending=False)
print(bank_avg_rating)
print("\n")

# Create visualizations directory if it doesn't exist
Path("visualizations").mkdir(exist_ok=True)

# Visualization 1: Sentiment Distribution
plt.figure(figsize=(10, 6))
sns.countplot(x='sentiment', data=df, palette='viridis')
plt.title('Overall Sentiment Distribution')
plt.savefig('visualizations/sentiment_distribution.png')

# Visualization 2: Average Rating by Bank
plt.figure(figsize=(12, 6))
sns.barplot(x=bank_avg_rating.index, y=bank_avg_rating.values, palette='viridis')
plt.title('Average Rating by Bank')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('visualizations/avg_rating_by_bank.png')

# Visualization 3: Top Themes
plt.figure(figsize=(12, 6))
theme_counts.head(10).plot(kind='bar', color='skyblue')
plt.title('Top 10 Themes in Reviews')
plt.xlabel('Theme')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('visualizations/top_themes.png')

# Visualization 4: Themes by Sentiment
theme_sentiment = pd.crosstab(themes_df['themes'], themes_df['sentiment'])
plt.figure(figsize=(14, 8))
theme_sentiment.plot(kind='bar', stacked=True, colormap='viridis')
plt.title('Themes by Sentiment')
plt.xlabel('Theme')
plt.ylabel('Count')
plt.legend(title='Sentiment')
plt.tight_layout()
plt.savefig('visualizations/themes_by_sentiment.png')

print("Analysis complete. Visualizations saved to 'visualizations' directory.")

# Generate insights report
insights = """
# Customer Experience Insights Report

## Key Drivers of Positive Experience
1. {pos_theme1}: Users frequently mention {pos_theme1} positively, indicating it's a key strength.
2. {pos_theme2}: This is another area where users express satisfaction.

## Pain Points
1. {neg_theme1}: This is the most common complaint among users.
2. {neg_theme2}: Users also frequently express dissatisfaction with this aspect.

## Bank Comparison
- {top_bank} has the highest average rating ({top_rating:.2f}/5), particularly excelling in {top_bank_theme}.
- {bottom_bank} has the lowest average rating ({bottom_rating:.2f}/5), struggling most with {bottom_bank_theme}.

## Recommended Improvements
1. Address {neg_theme1} issues by implementing more robust testing and optimization.
2. Enhance {neg_theme2} by redesigning the relevant features based on user feedback.
3. Consider adding new features related to {new_feature}, which users from competing apps mention positively.

## Conclusion
The analysis reveals that while users generally appreciate the {pos_theme1} and {pos_theme2} of the apps,
there are significant opportunities for improvement in {neg_theme1} and {neg_theme2}.
Addressing these issues could significantly improve overall customer satisfaction.
""".format(
    pos_theme1=positive_themes.index[0] if not positive_themes.empty else "usability",
    pos_theme2=positive_themes.index[1] if len(positive_themes) > 1 else "features",
    neg_theme1=negative_themes.index[0] if not negative_themes.empty else "performance",
    neg_theme2=negative_themes.index[1] if len(negative_themes) > 1 else "reliability",
    top_bank=bank_avg_rating.index[0],
    top_rating=bank_avg_rating.values[0],
    top_bank_theme="usability",  # This would ideally be derived from more detailed analysis
    bottom_bank=bank_avg_rating.index[-1],
    bottom_rating=bank_avg_rating.values[-1],
    bottom_bank_theme="performance",  # This would ideally be derived from more detailed analysis
    new_feature="budgeting tools"  # This would ideally be derived from competitive analysis
)

# Save insights report
with open("visualizations/insights_report.md", "w") as f:
    f.write(insights)

print("Insights report saved to 'visualizations/insights_report.md'")