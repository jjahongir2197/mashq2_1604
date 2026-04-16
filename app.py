from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return open("index.html").read()

@app.route("/add", methods=["POST"])
def add():
    son1 = int(request.form.get("son1"))
    son2 = int(request.form.get("son2"))

    natija = son1 + son2

    return f"Natija: {natija}"

app.run(debug=True)
