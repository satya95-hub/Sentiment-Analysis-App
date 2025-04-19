# model.py

import joblib
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\bnot\s+(\w+)', r'not_\1', text)
    text = re.sub(r'[^a-zA-Z_]', ' ', text)
    return ' '.join([word for word in text.split() if word not in stop_words])

# Load trained model and vectorizer
model = joblib.load('sentiment_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

def analyze_sentiment(review):
    cleaned = clean_text(review)
    vec = vectorizer.transform([cleaned])
    prediction = model.predict(vec)
    return prediction[0]
