from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_wtf import FlaskForm
from flask_bcrypt import Bcrypt #used for more security (hashed passwords)

DB_NAME = "database.db"

app = Flask(__name__)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
app.config["SECRET_KEY"] = "csgod"

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True, nullable=False)
    username = db.Column(db.String(150), unique = True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class SubscribeForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(max=150)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(max=150)], render_kw={"placeholder": "Password"})
    email = EmailField(validators=[InputRequired(), Length(max=150)], render_kw={"placeholder": "Email"})
    subscribe = SubmitField("Subscribe")

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if(existing_user_username):
            raise ValidationError(
                "This username already exists. Please choose a different one!"
            )

    # def validate_email(self, email):
    #     existing_user_email = User.query.filter_by(
    #         email=email.data).first()
    #     if(existing_user_email):
    #         raise ValidationError(
    #             "This email already exists. Please choose a different one!"
    #         ) 
    # The above function might not work

@app.route("/home")
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

@app.route("/subscribe", methods = ['GET', 'POST'])
def joinPage():
    form = SubscribeForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("subscribe.html", form=form)

# db.create_all()
app.debug = True
app.run(host = "0.0.0.0", port=8910)