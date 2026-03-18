from flask import Flask, render_template, request, jsonify
import os
from groq import Groq

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/explain", methods=["POST"])
def explain():

    data = request.json
    term = data.get("term")
    lang = data.get("lang")

    prompt = f"Explain {term} in simple {lang} language"

    try:

        client = Groq(
            api_key=os.environ.get("GROQ_API_KEY")
        )

        chat = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}]
        )

        result = chat.choices[0].message.content

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"result": "Error generating explanation"})


app = app