import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import (
    generate_password_hash, check_password_hash)
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/index")
def index():
    categories = list(mongo.db.categories.find())
    return render_template("index.html", categories=categories)


@app.route("/login", methods=["GET", "POST"])
def login():
    categories = list(mongo.db.categories.find())
    if request.method == "POST":
        current_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if current_user:
            if check_password_hash(
                    current_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for("profile", username=session["user"]))

            else:
                return redirect(url_for("login"))

        else:
            return redirect(url_for("login"))

    return render_template("login.html",  categories=categories)


@app.route("/register", methods=["GET", "POST"])
def register():
    categories = list(mongo.db.categories.find())
    if request.method == "POST":
        current_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if current_user:
            flash("Username exists already")
            return redirect(url_for("register"))

        register = {
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # new user to session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Completed")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html", categories=categories)


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["first_name"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/get_all_recipes")
def get_all_recipes():
    categories = list(mongo.db.categories.find())
    recipes = list(mongo.db.recipes.find())
    return render_template(
        "recipes.html", recipes=recipes, categories=categories)


@app.route("/categorised_recipes/<get_category_name>")
def categorised_recipes(get_category_name):
    categories = list(mongo.db.categories.find())
    category = get_category_name
    recipes = mongo.db.recipes.find({'category_name': get_category_name})
    return render_template(
        "categorised_recipes.html", categories=categories,
        recipes=recipes, category=category)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
