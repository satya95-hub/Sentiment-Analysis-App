from flask import Flask, render_template, request
from model import analyze_sentiment

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def predict():
    sentiment = None
    review = None
    show_curtain = True  # Show curtain on initial load

    if request.method == "POST":
        review = request.form["review"]
        sentiment = analyze_sentiment(review)

        if sentiment == "error":
            sentiment = None  # No result shown
        else:
            show_curtain = False  # Only hide curtain if input is valid

    return render_template("index.html", sentiment=sentiment, review=review, show_curtain=show_curtain)

if __name__ == "__main__":
    app.run(debug=True)
