from flask import Flask, request, render_template
from markupsafe import escape


app = Flask(__name__)
# __name__ is a special variable in Python that represents the name of the current module.
# When you run a Python script, the __name__ variable is set to "__main__". However, when you import a module,
# the __name__ variable is set to the name of the module. In this case, we are using __name__ to tell Flask where
# to look for templates and static files.


@app.route("/")
# decorator for the home page route.
# The @app.route("/") decorator tells Flask that this function should be called when the user visits
# the root URL ("/") of the application.

def home():
    return "<h1>Weclome to the Flask Framework</h1>"


@app.route("/about")
def about():
    return "<p>About Page</p>"


@app.route("/contact")
def contact():
    return "<p>Contact Page</p>"


@app.route("/myStory/<title>")
def my_story(title):
    return f"<h1>{title}</h1><p>My Story Page</p> this is my story page. I am a software developer with a passion for creating web applications using Flask.</p>"


@app.route("/hello")
def hello():
    name = request.args.get("name", "Flask")
    return f"<h1>Hello, {escape(name)}!</h1>"


# What is dynamic routing?
# Dynamic routing allows you to create routes that can accept parameters
# in the URL. This means that you can create a single route that can handle
# multiple URLs by using placeholders in the route definition. For example, you can
# create a route that accepts a username as a parameter and displays a personalized greeting.


@app.route("/user/<username>")
def user_profile(username):
    return f"<h1>Hello, {username}!</h1>"


# Templates
# Templates in Flask are used to separate the presentation layer (HTML) from the application logic (Python code).
# They allow you to create dynamic web pages by embedding Python code within HTML files. Flask uses the Jinja2
# templating engine, which provides a powerful way to generate HTML content based on data passed from
# the Flask application.
# You don't have to write HTML code directly in your Python functions. Instead, you can create separate HTML files
# (templates) and render them with dynamic data.

# Rendering templates in Flask is done using the render_template function.
# You can pass variables from your Flask application


# Profile route and function using template
@app.route("/profile/<string:username>/<int:user_id>")
def profile(username, user_id):
    return render_template("profile.html", username=username, user_id=user_id)


# To avoid repetition, use template inheritance. Create a base template (base.html) that
# contains the common structure of your web pages,and then extend this base template in your
# other templates (like profile.html). This way, you can maintain a consistent layout across your application and
# only define the unique content for each page in their
# respective templates.

# To ensure your server runs only if this script is executed directly
# (and not imported as a module), you can use the following code:

if __name__ == "__main__":
    app.run(debug=True)
