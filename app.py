# app.py
from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Put your OpenAI API key here
openai.api_key = "YOUR_API_KEY_HERE"

@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    if request.method == "POST":
        question = request.form["question"]
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful sports explainer."},
                {"role": "user", "content": question}
            ]
        )
        answer = response["choices"][0]["message"]["content"]

    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)