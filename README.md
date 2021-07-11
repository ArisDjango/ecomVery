# ecomVery
tes git push

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
- Testing


