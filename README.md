# ecomVery
new main

- Instalasi
    - mkdir ecomvery di local --> Buat repo baru git --> clone repo tsb ke local --> test push
    - cd ecomvery/ecomvery
    - pipenv --> pip install pipenv --> touch Pipfile --> pipenv lock --> pipenv install system
    - django-admin startproject ecomvery .
    - django-admin startapp store
- Model
    - Edit store/models
    - makemigrations --> migrate
    - set settings.static/media --> set ecomvery.url

- Admin
    - python manage.py createsuperuser
    - store.admin --> register model yg ingin ditampilkan
- Static/media set
    - set path di settings.py
    - setting url media
    - install pillow

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


