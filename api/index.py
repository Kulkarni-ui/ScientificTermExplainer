from flask import Flask, render_template
import os
from groq import Groq

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

@app.route("/")
def home():
    return render_template("index.html")

app = app