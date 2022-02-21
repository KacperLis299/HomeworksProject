from flask import Blueprint, render_template

home_blueprint = Blueprint('home_blueprint', __name__)


@home_blueprint.route("/")
def home():
    return render_template("home.html")


@home_blueprint.route("/about")
def about():
    return render_template("about.html")
