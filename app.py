import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        prof = request.form["prof"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(prof),
            temperature=0,
            max_tokens=1024
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(prof):
    return f'Расскажи о профессии {prof.capitalize()}'
