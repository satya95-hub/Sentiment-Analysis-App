# app.py
from flask import Flask, render_template, request
from model import analyze_sentiment

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def predict():
    sentiment = None
    review = None
    show_curtain = True  # Curtain should show on page load

    if request.method == "POST":
        review = request.form["review"]
        sentiment = analyze_sentiment(review)
        show_curtain = False  # Curtain will hide once the form is submitted
    
    return render_template("index.html", sentiment=sentiment, review=review, show_curtain=show_curtain)

if __name__ == "__main__":
    app.run(debug=True)
