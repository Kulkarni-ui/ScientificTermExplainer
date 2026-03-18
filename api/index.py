from flask import Flask, render_template, request, jsonify
import os
from groq import Groq
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static"),
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/explain", methods=["POST"])
def explain():

    data = request.json

    term = data.get("term")
    lang = data.get("lang")

    key = os.environ.get("GROQ_API_KEY")

    if not key:
        return jsonify({"error": "API key missing"})

    prompt = f"""
Explain "{term}" in {lang}.

Return JSON:
{{
"term":"",
"explanation":"",
"example":"",
"related_terms":[]
}}
"""

    try:

        client = Groq(api_key=key)

        chat = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}]
        )

        text = chat.choices[0].message.content

        try:
            result = json.loads(text)
        except:
            result = {
                "term": term,
                "explanation": text,
                "example": "",
                "related_terms": []
            }

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)})


handler = app