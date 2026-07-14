# Django
# Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.
# It follows the model-template-view (MTV) architectural pattern and provides an easy-to-use admin interface, ORM (Object-# Relational Mapping), and many built-in features for web development.
#
# MVT
# 1. Model: Represents the data structure and handles database interactions.
# The model defines the fields and behaviors of the data you’re storing. Django provides a powerful ORM that allows you to interact with the database using Python code instead of writing raw SQL queries.Additionally, models can include methods to perform operations on the data, such as validation, calculations, or custom queries.
#
# 2. View: Handles the logic and processing of user requests and returns responses.
# The view receives user input, processes it (e.g., querying the database, performing calculations), and prepares the data to be displayed. It acts as a bridge between the model and the template, ensuring that the right data is passed to the template for rendering. Views can be function-based or class-based, allowing developers to choose the approach that best fits their needs.
# 3. Template: Defines the presentation layer and renders the data to be displayed to the user.
# Templates are responsible for generating the HTML content that is sent to the user's browser. They use a templating language that allows developers to embed dynamic content, such as variables and control structures (e.g., loops and conditionals), within the HTML. Templates can also include static files like CSS and JavaScript to enhance the user interface and user experience.
#
# Folder strucutre
# A typical Django project folder structure includes the following components:
# level 1(main porject folder):
# - manage.py: A command-line utility that allows you to interact with your Django project. It provides various commands for tasks like running the development server, creating database migrations, and managing applications.
# - requirements.txt: A file that lists the Python packages and dependencies required for the project.
# - .gitignore: A file that specifies which files and directories should be ignored by version
# - porject-name/: The main project folder that contains the settings, URLs, and WSGI/ASGI configuration files.
#
# level 2(project folder):
# - __init__.py: An empty file that indicates that this directory should be treated as
# a Python package.
# - settings.py: The configuration file for the Django project, containing settings for database connections,
# - asgi.py: The ASGI (Asynchronous Server Gateway Interface) configuration file for the project, which allows for handling asynchronous requests and WebSocket connections.
# - urls.py: The URL configuration file that maps URLs to views in the project.
# - wsgi.py: The WSGI (Web Server Gateway Interface) configuration file for the project, which allows for handling synchronous requests and deploying the application to a web server.
# - views.py: A file that contains the view functions or classes responsible for processing user requests and returning responses.
#

