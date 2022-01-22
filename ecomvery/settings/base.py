"""
Django settings for ecomvery project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+%!zoo9&dimk(+$xuz^fzl)*jqg+izprg47jpf9sgna&gbti81'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['aris.com','localhost','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'ecommerce.apps.catalogue',
    #'ecommerce.apps.account',
    #'ecommerce.apps.checkout',
    #'ecommerce.apps.basket',
    #'ecommerce.apps.orders',
    'mptt',
    'store',
    'basket',
    'account',
    'orders',
    'catalogue',
    'checkout',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecomvery.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'store.views.categories',
                'store.context_processors.categories',
                'basket.context_processors.basket',
                #'ecommerce.apps.catalogue.context_processors.categories',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecomvery.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

#Basket session ID
BASKET_SESSION_ID = "basket"

# # Stripe Payment
# PUBLISHABLE_KEY = 'pk_test_51K6UYoJtaYn6oIYDaljcQ9JvftFKy6as4l0jSFRFCOL31wS9lepTffk3SkwkoCRYS82Ed15fPZxCSbj6o9jb6sLK00c1r3nNQF'
# SECRET_KEY = 'sk_test_51K6UYoJtaYn6oIYDB0iqTO5sx6MQvJLZzSHOBRW4TCjQOGgcFfSiebLAzHVIDJgsSauFpLyGkwkBIP2XPlofG3tZ00cEGplIfd'
# STRIPE_ENDPOINT_SECRET = 'whsec_ixaR99wdK9VFwr9WNf7PazkIwimAB0IG' # Dari stripe CLI
# # stripe listen --forward-to localhost:8000/payment/webhook/

# # Stripe Payment --> delete during part 8 paypal
# os.environ.setdefault('STRIPE_PUBLISHABLE_KEY', 'pk_test_51K6UYoJtaYn6oIYDaljcQ9JvftFKy6as4l0jSFRFCOL31wS9lepTffk3SkwkoCRYS82Ed15fPZxCSbj6o9jb6sLK00c1r3nNQF')
# STRIPE_SECRET_KEY = 'sk_test_51K6UYoJtaYn6oIYDB0iqTO5sx6MQvJLZzSHOBRW4TCjQOGgcFfSiebLAzHVIDJgsSauFpLyGkwkBIP2XPlofG3tZ00cEGplIfd'
# STRIPE_ENDPOINT_SECRET = 'whsec_ixaR99wdK9VFwr9WNf7PazkIwimAB0IG' # Dari stripe CLI
# # stripe listen --forward-to localhost:8000/payment/webhook/

# Custom user model
# AUTH_USER_MODEL = "account.Customer"
# AUTH_USER_MODEL = "account.UserBase" #during UUID
AUTH_USER_MODEL = "account.Customer"
LOGIN_REDIRECT_URL = "/account/dashboard"
LOGIN_URL = "/account/login/"


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email setting
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'