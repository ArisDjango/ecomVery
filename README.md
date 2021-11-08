# ecomVery
new main
## 1. Building models, views and testing
- DEVELOPMENT
    - Visual Studio Extensions
        - python (microsoft), ayu, django, sqlite
    - Check Python Version : `python3 --version`
    - Create Virtual Environment : 
        ```
        python3 -m venv venv
        source venv/bin/activate
        ```
    - Install Django : `pip install django`
    - Start Django Project:
        ```
        django-admin startproject ecomvery .

        ```
    - Create New Django App
        ```
        python manage.py startapp store

        ```
    - Building the Models
        ```
            - Edit store/models
            - makemigrations --> migrate
            - set settings.static/media --> set ecomvery.url

        ```
    - Install Pillow
    - Make Initial Migrations
    - Setup the Media Folder for Saving Images
        ```
        - set path di settings.py
        - setting url media
        ```
    - Django Admin Configuration
        ```
        - python manage.py createsuperuser
        - store.admin --> register model yg ingin ditampilkan
        ```

    - Testing part 1
        - install coverage
        - coverage run manage.py test
        - coverage run --omit='*/venv/*' manage.py test
        - Building Model Tests?

- URLs and Views
    - Intro and Visualising URLs, Views, Templates and Models
    - Configuring the URL Files
    - Building the Home View
    - Configure the Template Settings
    - Django Templating
    - Building the base.html page
    - Building the home.html page
    - Integrating Bootstrap to the Project
    - Developing the base and home page with Bootstrap
    - Developing the Category view
    - Making Data Available - Context Pre-processor
        - settings/template
    - Building the Products Data Grid
    - Building the Product Single Page View
    - Creating the detail.html Page
    - Building Dynamic Links - Linking Pages and Categories
    - Building the Category View and Template

- Testing Part 2 - Testing Views
    - Building Tests for Views
    - How to Skip Tests
    - Using the Test Client
    - Understanding HTML Response Codes
    - Using HttpRequest() to Test HTML Code
    - Using Request Factory Introduction and Test Example

- PEP 8 Python Style Guide
    - Introduction to PEP 8
    - Flake8 Install and Basic Usage
    - Installing and using isort

## 2. Build an ecommerce basket with session handling
- Refactoring Tasks (optional tasks):
    - Refactoring Introduction
        - code readibility
        - File names
        - Remove redundant code
        - Add features
- Preparing for refactoring
    - Downloading previous tutorial code
    - Open code with Visual studio Code
    - Build virtual environment and install dependencies
- Starting to refactor project
    - Reconfigure the context processor
        - Ubah pada settings> templates> store.views... ke store.context_processors...
        - Buat store>context_processors.py
        - import fungsi "categories" dari views ke store>context_processors.py
    - Remove redundant links from navbar
        - Menghapus link2 yang tidak digunakan
        - templates>store>base.html
    - Visual change to homepage element
    - Creating a new custom object manager
    - Removing comments from settings.py
    - Renaming views
    - SEO - Changing the page titles 
    - Changing the template names
    - Changing the URL structures - Store items
    - gitignore file
    - Model - adding a default image
    - Changing the URL structures - Store category
    - Creating a test to check AllOWED_HOSTS
    - Flake8 and isort - PEP 8 compliance
    - Testing - Run and Change test parameters
    - Setup static folder
    ```
    ****Important****
    Ajax will not work with the slim version of jQuery - minified version is okay.
    ******************
    ```

    - Updating the Bootstrap & jQuery CDN links
    - Finished refactoring

- Introducing Sessions (optional step):
    - Introduction to sessions
    - Visual explanation of sessions
    - Viewing the Django database - session table
    - Viewing the session in the browser console
    - Django required resources to enable sessions

- Development Part 1.0 (Preparing the project):
    - Introduction
    - Create a new app - basket
    - Remove unnecessary files
    - Configure the URL's for the basket
    - Building the basket summary view
    - Building the basket summary template
    - Making the basket icon/button for the navbar
    - VSC extension for formatting HTML/Python template files

- Development Part 1.2 (Building a Session):
    - Building sessions
    - Building the context_processor file
    - Testing the initial session setup

- Development Part 1.3 (Creating add functionality):
    - Building the add to cart button functionality (Ajax)
    - URL for a the add function
    - view for the add function
    - updating the basket class
    - Adding the Qty to the session data

- Development Part 2.0 (Deleting basket/session data):
    - Introduction - deleting session data
    - Creating the basket summary template
    - Iterating over the session data
    - Get the total price of the basket items  

- Development Part 2.1(Front-end - deleting basket/session data):
    - Introduction - Ajax for deleting items
    - Creating Ajax for deleting basket items
    - Building a basket URL
    - Creating a delete function in view
    - Handling remove items in the basket class
    - Resolving the unique DOM ID issue with Ajax
    - Removing elements from the page with JavaScript

- Development Part 3.0 (Updating basket/session data):
    - Introduction - updating session data
    - Capturing the user selection
    - Create a URL for updating data
    - Create the view function
    - Further developing the basket class
    - Developing the front-end code for update
    - Resolving known issues
    - Resolving final issue

- Testing
    - Introduction 
    - Running existing tests
    - Running coverage - assessing tests required
    - Building tests for the basket app