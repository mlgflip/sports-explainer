# app.py
from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# Use environment variable for OpenAI API key
import os
openai.api_key = os.getenv("OPENAI_API_KEY")
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
    # Correct host and port for Render
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
