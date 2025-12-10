from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

sentiment_model = pipeline("sentiment-analysis")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        text = request.form["text"]
        result = sentiment_model(text)[0]
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)