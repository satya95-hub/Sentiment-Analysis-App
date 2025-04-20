import joblib
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    
    # Custom handling for specific negation patterns (e.g., "not the worst")
    text = re.sub(r'\bnot the worst\b', 'neutral', text)  # Treat "not the worst" as neutral
    
    # General negation handling
    text = re.sub(r'\bnot\s+(\w+)', r'not_\1', text)  # "not" followed by a word
    text = re.sub(r'\bnot\b', 'not_', text)  # Handle standalone "not"
    
    # Remove non-alphabetic characters
    text = re.sub(r'[^a-zA-Z_]', ' ', text)
    
    # Remove stopwords
    return ' '.join([word for word in text.split() if word not in stop_words])


# Load model and vectorizer
model = joblib.load('sentiment_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

def analyze_sentiment(review):
    cleaned = clean_text(review)

    # Check if any word in the cleaned review exists in vectorizer vocabulary
    valid_tokens = [word for word in cleaned.split() if word in vectorizer.vocabulary_]
    if not valid_tokens:
        return 'unknown'

    vec = vectorizer.transform([' '.join(valid_tokens)])
    prediction = model.predict(vec)
    return prediction[0]
