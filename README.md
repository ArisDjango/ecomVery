# ecomVery
List
1. [ A. Building models, views and testing ](#A)
2. [ B. Build an ecommerce basket with session handling ](#B)
3. [ C. Build a user, payment and order management system](#C)

<a name="A"></a>
## 1. Building models, views and testing
- DEVELOPMENT
    - Visual Studio Extensions
        - python (microsoft), ayu, django, sqlite
    - Check Python Version : `python3 --version`
    - Create Virtual Environment : 
        - `python3 -m venv venv`
        - `source venv/bin/activate`
    - Install Django : `pip install django`
    - Start Django Project: `django-admin startproject ecomvery .`
    - Create New Django 'Store' App : `python manage.py startapp store`\
    - Building the Models
        - Edit store/models
        - makemigrations --> migrate
        - set settings.static/media --> set ecomvery.url
    - Install Pillow
    - Make Initial Migrations
    - Setup the Media Folder for Saving Images
        - set path di core > settings.py
        - setting url media
    - Django Admin Configuration
        - `python manage.py createsuperuser`
        - store > admin.py --> register model yg ingin ditampilkan
    - Testing part 1
        - install coverage
        - `coverage run manage.py test`
        - `coverage run --omit='*/venv/*' manage.py test`
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

<a name="B"></a>
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
        - hapus `test.py` dan `admin.py`
    - core basket urls --> ` core > urls.py > path('basket/', include('basket.urls', namespace='basket')),` --> semua url yg berhubungan dg basket diarahkan ke `basket > urls.py`
    - basket summary url --> `basket > urls.py > 'path('', views.basket_summary, name='basket_summary'),'`
    - basket summary view --> `basket > views.py > def basket_summary()'`
    - basket summary template --> `templates > store > basket > summary.html` --> basic saja, nanti di update di 2.0
    - Making the basket icon/button for the navbar --> `https://getbootstrap.com/docs/5.0/components/buttons/`
    - VSC extension for formatting HTML/Python template files
        - plugin -BEAUTIFY untuk merapikan html/js > `command: beautify file`

- Development Part 1.2 (Create a Session & Context processor):
    - Building sessions
        - `basket > basket.py`
        - `class Basket() > def __init__()` --> function yang diakses pertama kali
    - Building the context_processor file
        -
        ```
        fungsi context_processors adalah sebuah metode untuk mempermudah kita menampilkan data secara global tanpa harus membuat fungsi yang saama berulang kali di banyak views / templates.
        ```
        - `basket > context_processors.py > def basket()`
        - `core > TEMPLATES=[] > OPTIONS:{} > 'basket.context_processors.basket',` --> registrasi di core
    - Testing the initial session setup
        - `basket.py > 'def __init__'`
        - set skey --> `...basket = self.session['skey'] = {'number': 12345}`
        - cari session id di browser --> inspect/application/cookies
        - atau bisa cek di table database sqlite3 > django_session
        - `python manage.py shell`
            ```py
            from django.contrib.sessions.models import Session

            s = Session.objects.get(pk='i0zrp54n5lrynjkqe0eqfqqtm5qu2803')
            s.get_decoded()

            output = 12345
            ```
- Development Part 1.3 (Add to session functionality):
    - Building the add to basket button functionality (Ajax)
        - Tujuan: Memfungsikan tombol add to basket pada single.html
        - Pastikan versi jquery update pada `base.html`
        - basket add template -->
            - `templates > products > single.html > ...id="add-button" value="{{product.id}}..."`
            - `templates > products > single.html > AJAX Script -->$(document).on('click', '#add-button', function (e) { ...`
        - basket add url --> `basket > urls.py > 'path('add/',views.basket_add, name='basket_add'),'`
        - basket add view --> `basket > views.py > def basket_add()`
        - basket.py --> `basket > basket.py > basket class () --> def add()`
        - tes fungsi add to basket button pada single.html berupa (json response)  --> `basket > views.py > basket_add()`
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
        - Tujuan: Tes Fungsi `Quantity drop down select` pada single.html
        - Untuk tes console, tambahkan pada script ajax `console.log($('#select option: selected').text())`
        - `views.py > basket_add()`
            ```py
            ...
            basket.add(product=product, qty=product_qty)

            basketqty = basket.__len__()
            response = JsonResponse({'qty': basketqty})
            ```
        - Tes tombol quantity & add to basket, --> inspect > console, output: 1,2,3,4
        - Hasil akhir. pilih quantity --> tekan basket button = basket total. ketika memilih produk lain, akan otomatis menambah jumlah basket 
        

![session-delete](https://user-images.githubusercontent.com/24581953/145327750-fc8a2e58-2f12-4a15-be7a-af745bd3f319.jpg)
- Development Part 2.0 (Deleting basket/session data): test
    - Tujuan: Halaman kumpulan produk yang masuk di basket dg fitur add & delete button
    - Updating `templates > basket > summary.html`
        ```py
        {% for item in basket %}
        {% with product=item.product %}
        ...<div data-index="{{product.id}}..."
        ```
    - Iterating over the session data
        - `basket > basket.py >  def __iter__()`
    - Get the total price of the basket items
        - `basket > basket.py > def get_total_price()`

- Development Part 2.1(Front-end - deleting basket/session data):
    - Delete basket ( AJAX )
        - Tujuan: Memfungsikan tombol delete pada `templates > basket > summary.html`
        - basket delete template- -> updating summary.html
            - `templates > basket > summary.html > ...id="delete-button" data-index="{{product.id}}...`
            - `templates > basket > summary.html > AJAX script -->  $(document).on('click', '.delete-button', function (e) { ...`
        - basket delete url --> `basket > urls.py > 'path('delete/',views.basket_delete, name='basket_delete'),'`
        - basket delete view --> `basket > views.py > def basket_delete()`
    - Handling remove items in the basket class
        - `basket > basket.py > def delete()`
        - `basket > basket.py > def save()`
    - Resolving the unique DOM ID issue with Ajax
        - Issue : setelah tombol delete ditekan, harus di refresh dulu baru product bisa terhapus
        - `...data-index="{{product.id}}..."`

    - Removing elements from the page with JavaScript ( AJAX )
        - templates > basket > summary.html
        ```js
        ...
        success: function (json) {
            $('.product-item[data-index="' + prodid + '"]').remove();
            document.getElementById("subtotal").innerHTML = json.subtotal;
            document.getElementById("basket-qty").innerHTML = json.qty
        },
        ...
        ```

![sessions-update](https://user-images.githubusercontent.com/24581953/145501050-fc317711-948f-42b5-989b-84e8a09814e4.jpg)

- Development Part 3.0 (Updating basket/session data):
    - Capturing the user selection
    - Update basket ( AJAX )
        - Tujuan: Memfungsikan tombol quantity & update pada `templates > basket > summary.html`
        - basket update template- -> updating summary.html
            - `templates > basket > summary.html > ...id="update-button" data-index="{{product.id}}...`
            - `templates > basket > summary.html > AJAX script -->  $(document).on('click', '.update-button', function (e) {`
        - basket delete url --> `basket > urls.py > 'path('update/',views.basket_update, name='basket_update'),'`
        - basket delete view --> `basket > views.py > def basket_update()`
    - Updating the front-end code for update (AJAX code)
        - `templates > basket > summary.html`
        ```js
            success: function (json) {
            document.getElementById("basket-qty").innerHTML = json.qty
            document.getElementById("subtotal").innerHTML = json.subtotal
        },
        ```
        ```js
        ...
        Sub Total: Rp. <div id="subtotal" class="d-inline-flex">{{basket.get_total_price}}
        ...
        ```
    - Resolving known issues
    3.50
    harus di refresh baru berubah
    
    - Resolving final issue

- Testing
    - Introduction : python manage.py test
    - Running existing tests
        - store > tests > test_views.py
        ```py
         - deactivated test_view_function() after web using a session
         - add 'session test code' to test_homepage_html()

         from importlib import import_module
         from django.conf import settings

         ...
         def test_homepage_html()
         ...
         engine = import_module(settings.SESSION_ENGINE) 
         request.session = engine.SessionStore()
         ...

        ```
        
    - Running coverage - assessing tests required
        
        - `coverage run manage.py test`
        - `coverage run --omit='*/venv/*' manage.py test`
        - `coverage html`
        - htmlcov > index.html
        - Note:
            - (__init__.py di setiap folder test mengindikasikan folder tersebut yang akan dieksekusi untuk test)
            - setelah melakukan perubahan pada test langkah coverage diulangi sehingga html lama ter replace

    - Building tests for the basket app
        - `basket > test > test_views.py`
        - lakukan coverage

<a name="C"></a>
## 3. Build a user, payment and order management system
- screenshot `user`
- Changing the UI of the templates
    - static > core > css > base.css --> override bootstrap, dropdown menu, font, nav, logo, footer
    - static > basket > css > basket.css -->
    - Inject ke templates > store > base.html
- Finished updating templates
    -Code after refactoring https://github.com/veryacademy/django...

- Stage 1.0 - User management

    - Introduction
    - Start building the user app
        - `python manage.py startapp account`
        - core > register 'account'
    - Building the user model
        - account > models
            - class UserBase()
                - UserBase models
                - `pip install django-countries` --> untuk country fields
        
            - class CustomAccountManager()
                - def createSuperUser()
                - def createuser()
        - core > settings.py > 
            ```py
            AUTH_USER_MODEL = "account.UserBase"
            LOGIN_REDIRECT_URL = "/account/dashboard"
            LOGIN_URL = "/account/login/"
            ```
    - Updating the products model
        - store > models.py > class Product()
            - `created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='product_creator')`
    - User admin 
        - account > admin.py > `admin.site.register(UserBase)`
    - Migrate
        - `python manage.py makemigration && python manage.py migrate`
        - `python manage.py createsuperuser`
        - `python manage.py runserver`
        - 127.0.0.1/admin/ --> login menggunakan email

- Stage 1.1 - User signup with email confirmation

    - Start building user signup
    - Building the form
        - `account > forms.py > registrationForm()`
    - Building the view
        - `account > views.py > account_register()`
    - Generating hash keys in Django
        - account > token.py
        - `pip install six`
    - Finishing the email setup
        - `account > views.py`
        ```py
        from django.utils.encoding import force_bytes, force_text
        from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
        ```
        - `account > views.py > def account_register() > #setup email`
    - Building the email template
        - `templates > account > registration > account_activation_email.html`
    - Building the registration template
        - `templates > account > registration > register.html`
    - Building the registration URL
        - `core > urls.py > path('account/', include('account.urls', namespace='account')),`
        - `account > urls.py > path('register/', views.account_register, name='register'),`
    - Finishing the registration form
        - `account > forms.py > RegistrationForm() --> clean_username(), clean_password2(), clean_email(), __init__()`
    - Templating and final functions
        - `core > settings.py > EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'`
        - `account > urls.py > path('activate/<slug:uidb64>/<slug:token>)/', views.account_activate, name='activate'),`
        - `template > account > registration > account_activation_email.html`
        - `account > views.py > account_activate()`
        - `template > account > registration > activation_invalid.html`
        - `account > urls.py > path('dashboard/', views.dashboard, name='dashboard'),`
        - decorators
            - account > views.py
            ```py
            ...
            from django.contrib.auth.decorators import login_required
            ...
            @login_required
            def dashboard(request):
            ...
            
            

            ```
         
    - Building up the dashboard
        - `template > account > user > dashboard.html`

- Stage 1.2 - Login/Logout
    - Login
        - `account > urls.py > path('login/', auth_views.LoginView.as_view(template_name='account/registration/login.html', form_class=UserLoginForm), name='login'),`
    - Login form 
        - account > forms.py > 
            - `from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm,SetPasswordForm)`
            - `UserLoginForm()`
    - Login template
        - `template > account > registration > login.html`
    - Logout URL and link updates
        - `account > urls.py > path('logout/', auth_views.LogoutView.as_view(next_page='/account/login/'), name='logout'),`
        - templates > store > products > base.html >
        ```py
        ...
        <a type="button" role="button" href="{% url "account:logout" %}"
        ...
        ```

- Stage 1.3 Update/Edit and delete account
    - Edit user 
    - URL for edit user profile
        - `account > urls.py > path('profile/edit/', views.edit_details, name='edit_details'),`
    - Create view for profile edit
        - `account > views.py >`
            ```py
            ...
            @login_required
            def edit_details(request):
            ...
            ```
    - Create form for profile edit
        - `account > forms.py > UserEditForm()` 
    - Profile edit template
        - `templates > account > user > edit_details.html`
    - Delete user
        - `account > urls.py > path('profile/delete_user/', views.delete_user, name='delete_user'),`
        - `account > urls.py > path('profile/delete_confirm/', TemplateView.as_view(template_name="account/user/delete_confirm.html"), name='delete_confirmation'),`
        - `account > views >`
            ```py
            ...
            @login_required
            def delete_user(request):
            ...
            ```
        - `templates > account > user > delete_confirm.html`
    - Forgotten password
        - `account > urls.py >`
            ```py
            ...
            path('password_reset/', auth_views.PasswordResetView.as_view ...
            path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view...
            path('password_reset/password_reset_email_confirm/',TemplateView.as_view ...
            path('password_reset_confirm/Mg/password_reset_complete/',TemplateView.as_view...
            ...
            ```
        - `account > forms.py` >
            ```py
            PwdResetForm()
            PwdResetConfirmForm()
            ```
    
    - Email template
        - `templates > account > password_reset_email.html`
    - Password reset template
        - `templates > account > password_reset_form.html`
        - `templates > account > reset_status.html`

- Stage 2.0 - Payment
    - Introduction
    - Stripe payment stages
    - Build payment app
        - `python manage.py startapp payment`
        - core > registrasi 'payment'
    - Payment template
        - `templates > payment > home.html`
    - Payment URL
        - `core > urls.py > path('payment/', include('payment.urls', namespace='payment')),`
        - `payment > urls.py > path('', views.BasketView, name='basket'),`
    - Payment view
        ```py
        @login_required
        def BasketView(request):
        ```
    - Stripe Elements 
        - dashboard.stripe.com/test/apikeys --> publish key & secret key
        - 
            ```py
            def BasketView(request):
                ...
                stripe.api_key = '<SECRET KEY>'
                intent = stripe.PaymentIntent.create(
                    amount=total,
                    currency='gbp',
                    metadata={'userid': request.user.id}
                )

                return render(request, 'payment/home.html', {'client_secret': intent.client_secret})
            ```
        - `pip install stripe=2.6.3`
        - `templates > payment > home.html`
            - `<button id="submit" class="btn btn-primary w-100 fw-bold" data-secret="{{ client_secret }}">Pay</button>`
            -
            ```js
            <script>
                {% comment %} Make csrf token availble in JS files {% endcomment %}
                var CSRF_TOKEN = '{{ csrf_token }}';
            </script>
            <script src="https://js.stripe.com/v3/"></script>
            <script src="{% static 'payment/index.js' %}" data-rel-js></script>
            ```
        - `static > payment > index.js '
            ```js
            var stripe = Stripe(<PUBLISH KEY>)`
            ...
            ```
        - stripe.com/docs/stripe-js
        - lakukan transaksi
        - cek pada stripe.com apakah transaksi sudah masuk

    - Stripe CLI
        - DOC : https://stripe.com/docs/stripe-cli
        - Download the latest linux tar.gz file from https://github.com/stripe/stripe-cli/releases/latest
        - Unzip the file: tar -xvf stripe_X.X.X_linux_x86_64.tar.gz
        - Move ./stripe to your execution path. --> sudo mv stripe /usr/local/bin
        - terminal > stripe login
        - klik link auth, masukkan password di browser. Stripe CLI siap digunakan
        - Coba lakukan checkout
        - terminal > stripe listen --> setiap ada transaksi akan muncul
 
- Stage 3.0 Order capture/Management
    - Build orders app
        - `python manage.py startapp orders`
        - Registrasi di core
    - Order models
        - `orders > models.py`
        - makemigrations & migrate
    - Connect orders to payment
        - `orders > views.py`
        - `core > urls.py > path('orders/', include('orders.urls', namespace='orders')),`
        - `orders > urls.py > path('add/', views.add, name='add'),`
    - Setting up Stripe webhooks
        - `payment > views.py >`
        ```py
        @csrf_exempt
        def stripe_webhook(request):
            ...
            # Handle the event
        if event.type == 'payment_intent.succeeded':
            payment_confirmation(event.data.object.client_secret)
            ...
        ```
        - `orders > views.py > `
        ```py
        ...
        def payment_confirmation(data):
            Order.objects.filter(order_key=data).update(billing_status=True)
        ...
        ```
        - `payment > views.py`>
        ```py
        def order_placed(request):
            basket = Basket(request)
            basket.clear()
            return render(request, 'payment/orderplaced.html')

        ```
        - `templates > payment > orderplaced.html`
        - `payments > urls.py >`
            ```py        
            path('orderplaced/', views.order_placed, name='order_placed'),
            path('webhook/', views.stripe_webhook),
            ```
        - `basket > basket.py >`
        ```py
        def clear(self):
            # Remove basket from session
            del self.session['skey']
            self.save()
        ```
        - core > settings.py >
        ```py
        # Stripe Payment
        PUBLISHABLE_KEY = 'xxx'
        SECRET_KEY = 'xxx'
        STRIPE_ENDPOINT_SECRET = 'xxx'
        ```
        - `terminal > stripe listen --forward-to localhost:8000/payment/webhook/`
        - lakukan transaksi checkout, setelah berhasil akan redirect ke http://127.0.0.1:8000/payment/orderplaced/
        - pada http://127.0.0.1:8000/admin > orders, checklist Billing status seharusnya tercentang
        
    - Users orders setup in dashboard
        - core > settings.py > 
            ```py
            #Basket session ID
            BASKET_SESSION_ID = "basket"
            ```
        - templates > user > dashboard.html > {% for item in order.items.all %}
        - basket > basket.py > --ganti __init__ pada `skey`
        ```py
        from django.conf import settings

        ...
        def __init__(self, request):
            self.session = request.session
            basket = self.session.get(settings.BASKET_SESSION_ID)
            if settings.BASKET_SESSION_ID not in request.session:
                basket = self.session[settings.BASKET_SESSION_ID] = {}
            self.basket = basket
        ...
        def clear(self):
            #Remove basket from session
            del self.session[settings.BASKET_SESSION_ID]
            self.save()

        ```
    - Update basket payment with postage calculation
        - `python manage.py test`

<a name="D">Refactor</a>
## 4. Refactor
- Refactoring store templates
- Refactoring basket templates
- Refactoring account templates
- Refactoring payment templates

<a name="E">MPTT</a>
## 5. Multi-Product Types Database Implementation
- Introduction
    - Implementasinya pada sub category product, lebih mudah menentukan parent / childnya
- Content
- Preview of db schema
- Start-up project
- Black and isort vscode automation
- Sorting the requirements text
- Modularising settings.py
    - core > settings > __init__.py
    - move settings.py ke dir diatas, rename menjadi base.py
    - ubah basedir --> `BASE_DIR = Path(__file__).resolve().parent.parent.parent`
    - manage.py > `'DJANGO_SETTINGS_MODULE', 'ecomvery.settings.base'`
- Django-debug-toolbar
    - pip install django-debug-toolbar
    - pastikan core > settings --> DEBUG = True
    - core > settings > dev_debug.py
    - manage.py > `'DJANGO_SETTINGS_MODULE', 'ecomvery.settings.dev_debug'`
    - core > urls.py >  `path("__debug__/", include(debug_toolbar.urls)),`
- Database schema walkthrough
    - dbdiagram.io/d
    - _documentation > database_schema.txt
- Building the database
    - hapus model database lama
    - pip install django-mptt
    - store > models.py --> perubahan besar pada models
- Finish building database 
    - Migration : makemigrations && migrate
- Integrating db into templates intro
    - Setting up admin.py --> - menampilkan data models pada admin
    - Integrating db into templates - perubahan template tag merujuk pada models baru

<a name="F"></a>
## 6. CRUD and UUID - Managing multiple addresses
- Introduction
    - Preview of build features
        - Implementasinya adalah penggunaan custom id 
    - Workflow
    - Account model changes
- DB Development
    - Start changing the account table model
        - lihat table baru --> customer & address
    - Actually making changes (sorry about the chatting)
        - account > models.py
        - Perubahan besar, dimana replace `UserBase()` dengan `Customer()` dan `Address()`
    - Introducing the UUID field
        - pada Address() menguunakan 'UUIDField'
        - Berfungsi sebagai custom id
    - Fixing problems with the changes we made in the account model
        - Fixing code2 di file lain menyesuaikan perubahan yang ada di model
        - makemigrations && migrate 
    - Turn off the Django debug toolbar


- UI Changes

    - Making changes to the dashboard UI --> base.py
    - menampilkan nama user pada dashboard ketika login
    - templates > account > dashboard > dashboard.html
    - templates > account > sub_base.html

- CRUD

    - Building the URLS for the address CRUD system
        - account > urls.py
        - path("addresses/" ...
    - Add address 
        - account > forms.py > `class UserAddressForm(forms.ModelForm):...`
        - account > views > `def add_address(request):...`
        - urls
        - templates > account > dashboard > adresses.html
    - Edit address
        - account > views > `def edit_address(request):...`
        - url
        - templates > account > dashboard > edit_adresses.html
    - Delete address
        - account > views > `def delete_address(request, id):...`
        - url
    - Set default address
        - account > views > `def set_default(request, id):...`

<a name="G"></a>
## 7. Customer Wish List
- Introduction
- Understanding one-to-one fields
- Adding/migrating a one-to-one field in database
    - store > models.py > Product()
    - `users_wishlist = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="user_wishlist", blank=True)`
- Workflow for creating a Wish-List
- Setup the add_to_wishlist URL and view
    - account > urls.py > wishlist
- Moving to the front-end - add the Wish List button
    - templates > store > single.html
- Hook up the user dashboard with the Wish List functions
    - Menambahkan menu wish list di dashboard --> `templates > account > dashboard > dashboard.html`
    - Halaman wish list --> `templates > account > dashboard > user_wish_list.html`
    - views untuk wish list --> `account > views > wishlist() && add_to_wish_list() `
    - urls --> `account > urls.py > wishlist`
- Django message framework - implement messages
    - core > 
        - 'django.contrib.messages',
        - 'django.contrib.messages.middleware.MessageMiddleware',
    - handle pesan sukses dan delete wishlist --> `account > views > add_to_wish_list() `
    - alert ketika add wish list --> `templates > store > single.html`

<a name="H"></a>
## 8. Paypal
- Removing the payment app
    - remove setting stripe pada core>settings.py
    - remove payment url pada core
    - remove tag 'payment' pada templates > basket > summary.html
- Create new checkout app
    - python manage.py startapp checkout
    - register di core
- Building the associated checkout tables
    - checkout > models.py
- Checkout Admin table registration and data input
    - checkout > admin.py
    - checkout > urls.py
    - core > urls.py
- Checkout delivery page
    - checkout > views.py
- Checkout address page
- Checkout payment page
- PayPal 
- Integrating with Orders