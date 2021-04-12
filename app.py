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


def is_logged_in():
    """
    Check if the user is stored in session (logged in)
    """
    return session.get("user")


@app.route("/")
@app.route("/index")
def index():
    """
    Index/Home page
    """
    categories = list(mongo.db.categories.find())
    return render_template("index.html", categories=categories)


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    login function's core taken from TaskManager|miniproject
    Logs user into website
    """
    if request.method == "POST":
        # check if user already in db
        current_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if current_user:
            # be sure passwords matching
            if check_password_hash(
                    current_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                            request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))

            else:
                # passwords not matching
                flash("The user name or password is incorrect")
                return redirect(url_for("login"))

        else:
            # user not existing
            flash("The user name or password is incorrect")
            return redirect(url_for("login"))

    categories = list(mongo.db.categories.find())
    return render_template("login.html",  categories=categories)


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    User's profile displays user's uploaded recipes
    """
    # getting session user's username from database
    if is_logged_in():
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        recipes = mongo.db.recipes.find({'username': username})
        return render_template(
            "profile.html", username=username, recipes=recipes)
    return redirect(url_for("login"))


@app.route("/user_recipes/<user_username>", methods=["GET", "POST"])
def user_recipes(user_username):
    """
    Allows users to see other users recipes
    """
    user = mongo.db.users.find_one({"username": user_username})
    username = mongo.db.users.find_one(
        {"username": user_username})["username"]
    recipes = mongo.db.recipes.find({"username": user_username})
    return render_template(
        "user_recipes.html", user=user, username=username, recipes=recipes)


@app.route("/logout")
def logout():
    """
    Remove user from session cookie
    Logout function's core taken from TaskManager|miniproject
    """
    session.pop("user")
    flash("See you comming back")
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Allows users to create account in a website
    register function's core taken from TaskManager|miniproject
    """
    categories = list(mongo.db.categories.find())
    # check if username already in database
    if request.method == "POST":
        current_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if current_user:
            flash("That username already exists")
            return redirect(url_for("register"))

        register = {
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "favourite_recipes": []
        }

        mongo.db.users.insert_one(register)

        # add new user to session cookie
        session["user"] = request.form.get("username").lower()
        flash("User Registration Successful! Please Login")
        return redirect(url_for("login"))

    return render_template("register.html", categories=categories)


@app.route("/get_all_recipes")
def get_all_recipes():
    categories = list(mongo.db.categories.find())
    recipes = list(mongo.db.recipes.find())

    return render_template(
        "recipes.html", recipes=recipes, categories=categories)


@app.route("/recipe/<recipe_id>", methods=["GET", "POST"])
def recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    return render_template("recipe.html", recipe=recipe)


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


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "username": session["user"],
            "rec_img": request.form.get("rec_img"),
            "cuisine_name": request.form.get("cuisine_name"),
            "category_name": request.form.get("category_name"),
            "description": request.form.get("description"),
            "rec_name": request.form.get("rec_name"),
            "level": request.form.get("level"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "serves": request.form.get("serves"),
            "methods": request.form.get("method"),
            "ingredients": request.form.get("ingredients")
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Your new recipe added")
        return redirect(url_for("profile", username=session["user"]))

    categories = list(mongo.db.categories.find())
    return render_template("add_recipe.html", categories=categories)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        updated = {
            "username": session["user"],
            "rec_img": request.form.get("rec_img"),
            "cuisine_name": request.form.get("cuisine_name"),
            "category_name": request.form.get("category_name"),
            "description": request.form.get("description"),
            "rec_name": request.form.get("rec_name"),
            "level": request.form.get("level"),
            "prep_time": int(request.form.get("prep_time")),
            "cook_time": int(request.form.get("cook_time")),
            "serves": int(request.form.get("serves")),
            "methods": request.form.get("method"),
            "ingredients": request.form.get("ingredients")
        }

        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, updated)
        flash("Recipe's details saved")
        return redirect(url_for('profile', username=session['user']))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find()
    return render_template(
        "edit_recipe.html", recipe=recipe,
        categories=categories)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Your recipe deleted")
    return redirect(url_for('profile', username=session['user']))


@ app.errorhandler(404)
def page_not_found(error):
    # Renders error page when error 404 occurs
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
