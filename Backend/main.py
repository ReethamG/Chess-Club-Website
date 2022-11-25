from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config["SECRET_KEY"] = "csgod"

@app.route("/")
def homePage():
    return render_template("index.html")

# @app.route("")

app.run(host = "0.0.0.0")