from flask import Flask, render_template, request, jsonify
import os
from groq import Groq
import json

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)


# ---------------- HOME ----------------

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- API ----------------

@app.route("/api/explain", methods=["POST"])
def explain():

    data = request.json

    term = data.get("term")
    lang = data.get("lang")

    key = os.environ.get("GROQ_API_KEY")

    if not key:
        return jsonify({
            "error": "API key missing"
        })

    prompt = f"""
Explain the scientific term "{term}" in {lang} language.

Return ONLY JSON in this format:

{{
"term": "",
"explanation": "",
"example": "",
"related_terms": ["", "", ""]
}}
"""

    try:

        client = Groq(api_key=key)

        chat = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        text = chat.choices[0].message.content

        # Try parsing JSON
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

        print("ERROR:", e)

        return jsonify({
            "error": "Error generating explanation"
        })


# IMPORTANT FOR VERCEL
handler = app