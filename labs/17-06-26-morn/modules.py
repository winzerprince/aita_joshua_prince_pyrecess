# Modules
#
# Modules help orgainize code into separate files and namespaces.
# They allow you to reuse code across different programs and projects.
# They can be both inbuilt and user-defined/external modules.
# Thy are accessible through the import statement.
#
# Why do we need to import modules?
# 1. To use functions, classes, and variables defined in other files.
# 2. To avoid code duplication and promote code reusability.
# 3. To organize code into logical units, making it easier to read and maintain.
#
# How to import modules?
# You can import and use module primarily in three ways:
# 1. import module_name
# 2. from module_name import function_name
# 3. from module_name import *
#
# How to import external modules?
# You can use the pip package manager to install external modules from the Python Package Index
# (PPyPI). For example, to install the requests module, you can run the following command in your terminal:
# pip install requests
# Pouplar external modules include:
# 1. requests: for making HTTP requests.
# 2. numpy: for numerical computing and data analysis.
# 3. pandas: for data manipulation and analysis.
# 4. matplotlib: for data visualization.
# 5. scikit-learn: for machine learning and data mining.
# 6. tensorflow: for machine learning and deep learning.
# 7. flask: for web development.
# 8. django: for web development.
#
# Some useful pip commands:
# 1. pip install package_name: to install a package.
# 2. pip uninstall package_name: to uninstall a package.
# 3. pip list: to list all installed packages.
# 4. pip show package_name: to show information about a package.
# 5. pip freeze: to list all installed packages and their versions.
# 6. pip install -r requirements.txt: to install packages from a requirements file.
# 7. pip install --upgrade package_name: to upgrade a package to the latest version.
# 8. pip install package_name==version: to install a specific version of a package.
#
# Importing specific fucntions from a module
# You can import specific functions and identifiers from a module using the from keyword.
# This allows you to use the function without having to prefix it with the module name.
# For example, if you want to use the sqrt function from the math module, you can do the following:
# from math import sqrt
# from math import pi
#
# To view inbuilt modules use the command help('modules') in the Python interpreter.
print(help("modules"))
