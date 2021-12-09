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
        - getbootstrap.com
        - copy css url pada bootstrap ke base.html
        - copy js (separate) ke base.html
        - Pada Body silahkan cari template yang sesuai
    - Developing the base and home page with Bootstrap
    - Developing the Category view
    - Making Data Available - Context Pre-processor
        - agar menu bisa tampil di semua page
        - settings/template
        - `store.views.category` --> `store.context_processors.categories`
    - Building the Products Data Grid
        - membuat grid untuk product di home.html
    - Building the Product Single Page View
        - url.py, views.py, product details
    - Creating the detail.html Page
        - templates/detail.html
    - Building Dynamic Links - Linking Pages and Categories
        - product.get_absolute_url
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
    - Flake8 Install and Basic Usage--> pip install flake8
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
        ```py
        class ProductManager(models.Manager):
        def get_queryset(self):
            return super(ProductManager, self).get_queryset().filter(is_active=True)
        ```
    - Removing comments from settings.py
    - Renaming views
        - all_product --> product_all
    - SEO - Changing the page titles 
    - Changing the template names
        - details.html --> single.html
    - Changing the URL structures - Store items
        - Menghapus 'item' pada path url, sehingga url akan langsung mengambil slug, localhost/item/react-buku --> localhost/react-buku
    - gitignore file
    - Model - adding a default image
        - default='images/default.png'
    - Changing the URL structures - Store category
        - ('search/<slug>... --> ('shop/<slug
    - Creating a test to check AllOWED_HOSTS
        - test host yang diijinkan
    - Flake8 and isort - PEP 8 compliance
        - isort .
    - Testing - Run and Change test parameters
        - `python manage.py tests`
    - Setup static folder
        - Jika membutuhkan file static, biasanya untuk css dan js
        - setting.py lalu buat folder static
    ```
    ****Important****
    Ajax will not work with the slim version of jQuery - minified version is okay.
    ******************
    ```

    - Updating the Bootstrap & jQuery CDN links
        - code.jquery.com --> minified --> copy script
        - Paste pada base.html --> <script>
    - Finished refactoring
        - kode mudah dibaca
        - penamaan files
        - menghilangkan kode yang tumpang tindih/redundant
        - menambahkan fitur
- Introducing Sessions (optional step):
    - Pengenalan session
        - session adalah informasi yang bersifat sementara dan interaktif
        - satu user per session - melakukan perubahan data berdasarkan per kunjungan user
        - Menyimpan data pada server-side
        - User menerima session ID
        - session ID dibutuhkan untuk pengambilan data
    - Visual explanation of sessions - penjelasan
         - ![session](https://user-images.githubusercontent.com/24581953/143838596-0e442daf-eec2-46ab-b222-b0e3bf1d0177.jpg)
    - Viewing the Django database - session table
        - plugin SQLlite-vscode
        - sudo install sqlite
        - table django_session
        - cek session by shell:
            - python manage.py shell
            ```
            from django.contrib.sessions.models import Session
            s = Session.objects.get(pk='5n6oxua39ths121v1r2ptjb68d9kqm5w')
            s.get_decoded()
            ```
    - Viewing the session in the browser console
    ![sessions](https://user-images.githubusercontent.com/24581953/144684799-90811cde-912f-468f-8c8d-ab17530054ea.jpg)
    ![sessions2](https://user-images.githubusercontent.com/24581953/144684821-fc5f9842-bd08-41ae-b1bc-32ad6db55957.jpg)
    - Django required resources to enable sessions
    ![sessions3](https://user-images.githubusercontent.com/24581953/144684838-73c4cf78-6958-4c1d-9180-d7601df66e5b.jpg)

![session part1](https://user-images.githubusercontent.com/24581953/145327404-5552acb6-0144-43ee-af71-a280f3cf0731.jpg)
- Development Part 1.0 (Setup):
    - Introduction
   

    - Create a new app - basket
        - `python manage.py createapp basket`
    - Remove unnecessary files
        - hapus test.py dan admin.py
    - Configure the URL's for the basket
        - buat basket.py
        - routing urls.py core --> include basket.urls.py
    - Building the basket summary view (basket/views.py)
    - Building the basket summary template (templates/store/basket/summary.html)
    - Making the basket icon/button for the navbar
        - https://getbootstrap.com/docs/5.0/components/buttons/
    - VSC extension for formatting HTML/Python template files
        - plugin -BEAUTIFY untuk merapikan html/js > command: beautify file

- Development Part 1.2 (Create a Session & Context processor):
    - Building sessions
        - basket/basket.py
        - class Basket() --> `def __init__`
    - Building the context_processor file
        - 
        ```
        fungsi context_processors adalah sebuah metode untuk mempermudah kita menampilkan data secara global tanpa harus membuat fungsi yang saama berulang kali di banyak views / templates.
        ```
        - basket/context_processors.py --> buat def basket()
        - core>templates>options>context_processors>'basket.context_processors.basket',
    - Testing the initial session setup
        - basket.py --> `def __init__`
        - set skey --> `...basket = self.session['skey'] = {'number': 12345}`
        - cari session id di browser --> inspect/application/cookies
        - atau bisa cek di table database django_session
        - python manage.py shell
        ```py
        from django.contrib.sessions.models import Session

        s = Session.objects.get(pk='i0zrp54n5lrynjkqe0eqfqqtm5qu2803')
        s.get_decoded()
        ```


- Development Part 1.3 (Add to session functionality):
    - Building the add to cart button functionality (Ajax)
        - tombol add to basket --> single.html
        - Pastikan versi jquery update pada base.html
        - single.html, button add to basket --> value = {{product.id}}
        - single.html, tambahkan script ajax pada bagian bawah
    - URL for a the add() 
    - view for the add()
    - updating the basket class ()
        - tes fungsi add to basket button pada single.html berupa (json response)  --> views.py/basket_add()
        ```py
        from django.http import JsonResponse
        ...
        response = JsonResponse({'test':'data'})
        return response
        ```
        ```py
        python manage.py shell

        # Sebelum button 'add to basket' di tekan
        from django.contrib.sessions.models import Session
        s = Session.objects.get(pk='i0zrp54n5lrynjkqe0eqfqqtm5qu2803')
        s.get_decoded()
        {'skey': {}} # kosong

        # Setelah button 'add to basket' di tekan
        {'skey': {'1': {'price': '40.00', 'qty': 1}}} 
        ```
    - Adding the Qty to the session data
        - Tes Fungsi `Quantity drop down select` pada single.html
        - tambahkan pada script ajax `console.log($('#select option: selected').text())`
        - views.py > basket_add()
            ```py
            ...
            basket.add(product=product, qty=product_qty)

            basketqty = basket.__len__()
            response = JsonResponse({'qty': basketqty})
            ```
        - Tes tombol quantity/add to basket, --> inspect > console, output: 1,2,3,4
        - Hasil akhir. quantity --> basket button = basket total. ketika memilih produk lain, akan otomatis menambah jumlah basket 
        

![session-delete](https://user-images.githubusercontent.com/24581953/145327750-fc8a2e58-2f12-4a15-be7a-af745bd3f319.jpg)
- Development Part 2.0 (Deleting basket/session data): test
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
