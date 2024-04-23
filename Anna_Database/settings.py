"""
Django settings for Anna_Database project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-pcez^&u2fwxtw55jw5%s_p0f$ifjfk$u+#)^n_3@veg+jy7l0k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'crispy_forms',
    'import_export',
    'Anna.apps.AnnaConfig',
    'Portfolio.apps.PortfolioConfig'
]
LOGIN_REDIRECT_URL = 'home' #MAIN INDEX
ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login' #lOGOUT
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_EMAIL_REQUIRED = True
SOCIALACCOUNT_EMAIL_VERIFICATION = False
ACCOUNT_SESSION_REMEMBER = True
SITE_ID = 1
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Anna_Database.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'Templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'Anna_Database.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Manila'
USE_I18N = True
USE_TZ = True
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'Anna_Database/static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static') # Automatically Csreated on Production
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'argonfernando453@gmail.com'
EMAIL_HOST_PASSWORD = 'oxrkklcttqackitg'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'System Messages'



JAZZMIN_SETTINGS = {
    "site_title": "My Portfolio",
    "site_header": "My Portfolio",
    "copyright": "Analyn Decierdo",
    "welcome_sign": "Welcome Analyn Decierdo",
    "site_logo": "assets/img/ana.png",
    "site_logo_classes": "img-circle",
    "site_brand":"Analyn Decierdo",
    #--------------
    "hide_models": ["account.emailaddress","auth.Group","auth.user","socialaccount.socialaccount","socialaccount.socialtoken","socialaccount.socialapp"],
    "show_ui_builder": False,
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Live View", "url": "google.com", "new_window": True},

    ],
    "changeform_format": "horizontal_tabs",
    "order_with_respect_to": ["OpenCv","Animations","Public", "Thesis"],
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-chevron-circle-right",
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-danger",
    "navbar": "navbar-secondary navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": True,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-lime",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "simplex",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-success"
    }
}
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
