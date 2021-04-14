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
 
## Design
 #### Colors
 ![Pallete](static/css/images/pallete-readme.png)

 I chose these shades to create warmth and depth. Looks elegant and at the same time reminds colors of nature.

 #### Backgrounds

 I chose background images which represents food, like herbs and peppers. In most pages I used marble table surface image.

## Features

 ### Existing Features

 * Navbar - provides easy navigation thru the webpage, for non-registred/registred users. By using navbar user can go to any page of website. Contains logo CookEasy link, which link to index page.
 * Index page - welcomes new and current users, provides information what users can do on website. Top section greets and provides button for registration Index page promotes brand betterkichen, contains button (for design purposes, no link) to link users to betterkitchen website.
 * Recipes page - contains all users recipes which currently in database. Each recipe has a card, which contains recipe image, name, small description, number of servings, cooking time, difficulty level. Recipe name links to individual recipe view.
 * Categorised recipes page - contains category's name header and recipes cards, recipes displayed matches category e.g. All-in-one, Cheap Solution, Vegetarian, Vegan...
 * Recipe page - shows individual recipe, contains image, recipe name, category, creator, cuisine, cooking time, prep-time, servings, ingredients,preparation steps. If user non-registered buttons not provided. If user are not a recipe creator, page provides button with heart/broken-heart icon for user to add or remove recipe to/from his Favourite recipes list. If user is recipe creator, page provides two buttons. One button lets edit recipe, other button with trash bin icon, lets user to delete recipe.
 * User Recipes page - when user opens individual recipe, she/he can click on created by: link, which links to recipe's creator profile. Which contains all creator's recipes. Page displays user's header, and recipes cards.
 * Profile page - contains header, button with folder icon to add recipe. Heart icon button to link user to his/hers Favourite recipes page.
 * Favourites page - only if user registered he/she can have Favourite recipes page. Contains header, button to add recipe and recipe card with Favourite recipes.
 * Add/Edit recipe pages - add recipe page has form with input fields for user to fill in new recipe details, and add recipe button. Edit recipe also contains same form, but imput fields already has content which can be modified, also contains add recipe button.
 * Register page - contains form where new user can fill in his details and create an account. Form has a link on the bottom for user to log in if she/he already registered to a website. Form also contains Register button.
 * Login page - displays form where registered user can fill in his username and password and login to profile. Form has a link to a registration page on the bottom, for non-registered users. Form has login button.
 * Footer - displays CookEasy address, phone number, and email with icons, social media links. Footer has contact details for betterkithen (promoted brand) shop. 

 ### Future Features
 * Add rating functionality, and let users leave comments for recipes.
 * Let user to change their username, email address, or reset password
 * Let user to download recipe as PDF file.
