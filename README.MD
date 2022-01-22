# Ecommerce Project - paypal integration

## Instalasi
- set workspace
    - clone project dari github
    - cd ecomvery
    - python -m venv venv
    - source venv/bin/activate
- Install dependensi
    - pip install django==3.2.7
    - pip install -r requirements.txt --> pastikan semua aplikasi berhasil terinstall. lakukan manual jika ada yang gagal
    - pip freeze > requirements.txt (optional)
    - python manage.py migrate
- Membuat user admin
    - python manage.py createsuperuser
- Run apps
    - python manage.py runserver
    - 127.0.0.1:8000/admin/
    - Isi data : Categories, product, product types, delivery options

## Docs
- Django 3
- sqlite
- bootsrap 5
- django mptt
- stripe (non aktif)
- paypal
