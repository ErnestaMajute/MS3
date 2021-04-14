# CookEasy

[This website](https://em-cookbook.herokuapp.com/index) is a project of website with recipes. Purpose of this project is to let user create, read, update and delete recipes. Non-registred users are able to browse recipes, while registred user are able to create and manipulate their recipes.

## UX


Goal of this website is to provide users with visually appealing recipe website, where user would be able to navigate easily. As well website promotes a brand of cooking accessories.

#### User Stories:

1. As a non-registered user I would like to browse recipes.
2. As a non-registered user I would like to be able easily register an account.  
3. As a non-registred/registered user I would like to chose a category of recipes.
4. As a non-registerd/registered user I would like to search for recipes with keyword.
5. As a non-registered/registered user, I would like to be able to browse profile of recipe's creator.
6. As a registered user I would like to view and add other user's recipe to my Favourites list.
7. As a registered user I would like to add, edit and delete my recipes.
8. As a registered user I would like to see my uploaded recipes in my profile page.
9. As a registered user I would like easily login or logout.



#### Functions(based on user stories):

 Basic requirement for this webpage is perform CRUD operations. User are able to register and login to his account. Non-registered/registered users are able to easily browse thru categories in a navigation bar (Categories dropdown), search for recipes with keyword. When recipes header link clicked, single recipe view opens up.
 Registered users are able to add, edit and delete their recipes. As well user are able to add his favourite recipe to his Favourite recipes list. User can browse thru other user's profile and see user's recipes. Only regitered users are able to add, edit and delete their recipes. Registered users are able to see all their uploaded recipes in their profile page. For registered users it's easy login and log out, by using button and form.

#### Content (based on user stories):

 * recipes page: displays all recipes. Available for all users.
 * recipe page: displays individual, chosen recipe: image, recipe name, category, creator, cuisine, cooking time, prep-time, servings, ingredients,preparation steps. If user is a creator of recipe, can click buttons to edit or delete recipe.
 * user_recipes page: displays other user recipes, linked from recipe(creator link).
 * edit_recipe page: user able edit his recipe.
 * Navigation bar for registered user: 
    * CookEasy logo: links to home/index page
    * Categories: all recipes categorised. User can choose suitable category.
    * Recipes: displays all recipes from database.
    * Add Recipe: page with form, where user are able fill in his new recipe details.
    * Profile: page which displays user's uploaded recipes.
    * Favourites: page displays Favourite recipes, which were added by user.
    * Log Out: user able to Log Out from his profile.
 * Navigation bar for non-registered user:
    * CookEasy logo: links to home/index page
    * Categories: all recipes categorised. User can choose suitable category.
    * Recipes: displays all recipes from database.
    * Log In: opens page where user fill's in his username and password
    * Register: opens page where user can fill in his details and create an account
 
