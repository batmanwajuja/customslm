# dashboard/app.py

from flask import Flask, render_template
import os

app = Flask(__name__)

LOG_FILE = os.path.abspath("logs/activity.log")

@app.route("/")
def index():
    try:
        with open(LOG_FILE, "r") as f:
            lines = f.readlines()[-100:]  # Show last 100 entries
    except FileNotFoundError:
        lines = ["No activity yet."]
    return render_template("index.html", logs=lines)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
