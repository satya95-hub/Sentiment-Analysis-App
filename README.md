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

The project is organized as follows:

app.py: The main Flask application that runs the web server.

model.py: Contains the logic for the sentiment analysis model.

train_model.py: Script used to train the machine learning model.

Folder Structure
templates/: Contains HTML templates for the frontend.

index.html: The main HTML page for the frontend.

static/: Stores static files like CSS and JavaScript.

css/: Contains the styles for the frontend.

style.css: Styling file for the frontend.

js/: JavaScript for frontend interactivity.

script.js: Contains the JavaScript logic.

sentiment_model.pkl: The saved machine learning model.

vectorizer.pkl: The saved text vectorizer for processing input text.

README.md: This file containing documentation about the project.

.gitignore: Specifies which files/folders to ignore when using Git.

