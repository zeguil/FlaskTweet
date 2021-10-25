from flask import render_template
from app import app


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test/<name>")
def test(name):
    return f"<h1>Olá {name}</h1>"

@app.route("/login")
def login():
    return render_template("login.html")
