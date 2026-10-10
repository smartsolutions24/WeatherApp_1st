from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    api_key = os.getenv("API_KEY")
    return render_template("index1.html", api_key=api_key)

if __name__ == "__main__":
    app.run(debug=True)
