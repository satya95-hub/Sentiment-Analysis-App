# Sentiment Analysis App 💬

This is a web-based sentiment analysis tool that analyzes Amazon product reviews and predicts whether the sentiment is **Positive**, **Negative**, or **Neutral**.

## 🚀 Technologies Used
- Python
- Flask
- HTML/CSS/JavaScript
- Machine Learning (Logistic Regression)
- scikit-learn
- Bootstrap

## 📂 Dataset
The dataset used in this project is **Amazon Product Reviews**.

👉 [Click here to download Reviews.csv](https://drive.google.com/file/d/11Awyzblr2PI5bC1NG5MYhdJy9Y2rl4oo/view?usp=sharing)

> ⚠️ Note: The dataset was too large to upload directly to GitHub.

## 🔥 Features
- Takes review input from user
- Analyzes sentiment using trained model
- Displays result on a stylish frontend
- Includes smooth scrolling and transitions

## ✨ Project Structure

Sentiment-Analysis-App/
│
├── app.py                  # Main Flask application
├── model.py                # Sentiment analysis model logic
├── train_model.py          # Script to train the ML model
│
├── templates/              # HTML templates
│   └── index.html          # Main frontend HTML page
│
├── static/                 # Static files like CSS and JS
│   ├── css/
│   │   └── style.css       # Styling for the frontend
│   └── js/
│       └── script.js       # JavaScript for frontend interactivity
│
├── sentiment_model.pkl     # Saved machine learning model
├── vectorizer.pkl          # Saved text vectorizer
├── README.md               # Project documentation
└── .gitignore              # Git ignore rules
