from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "csgod"

@app.route("/")
def homePage():
    return render_template("index.html")

@app.route("/about")
def aboutPage():
    return render_template("about.html")

@app.route("/opportunities")
def opportunitiesPage():
    return render_template("opportunities.html")

@app.route("/resources")
def resourcesPage():
    return render_template("resources.html")

@app.route("/join")
def joinPage():
    return render_template("subscribe.html")

app.debug = True
app.run(host = "0.0.0.0", port=8910)