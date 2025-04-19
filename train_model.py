import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = re.sub(r"\'", "", text)
    text = re.sub(r'\bnot\s+(\w+)', r'not_\1', text)
    text = re.sub(r'(.)\1{2,}', r'\1', text)  # goooood -> good
    text = re.sub(r'[^a-zA-Z_]', ' ', text)
    return ' '.join([word for word in text.split() if word not in stop_words])

# Load and preprocess
df = pd.read_csv('Reviews.csv')[['Text', 'Score']].dropna()
df['sentiment'] = df['Score'].apply(lambda s: 'Negative' if s <= 2 else ('Neutral' if s == 3 else 'Positive'))
df['cleaned_text'] = df['Text'].apply(clean_text)

X = df['cleaned_text']
y = df['sentiment']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# TF-IDF with trigrams
vectorizer = TfidfVectorizer(ngram_range=(1, 3), max_features=15000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Logistic Regression
model = LogisticRegression(C=1.0, max_iter=1000, solver='liblinear')
model.fit(X_train_vec, y_train)

# Save
joblib.dump(model, 'sentiment_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')
