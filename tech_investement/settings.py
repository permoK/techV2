"""
Django settings for tech_investement project.

Generated by 'django-admin startproject' using Django 3.2.21.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ixbwzzns+pcr206)uam#@gftm&h3!k711!x290@z%w-=z#e=5+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# <<<<<<< master
ALLOWED_HOSTS = ["192.168.100.119", "127.0.0.1","192.168.16.107","192.168.16.105","192.168.100.119","192.168.43.53","10.0.39.242", ".vercel.app","*", "codius.up.railway.app","codius.tech"]
# =======

# ALLOWED_HOSTS = ["192.168.100.119", "127.0.0.1","192.168.16.102","mykey.pythonanywhere.com"]
# >>>>>>> main

# CORS_ORIGIN_WHITELIST = [
#     'https://codius.up.railway.app',
# ]

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    #     My apps
    'widget_tweaks',
    'investor.apps.InvestorConfig',

    # 'corsheaders',

    # ALLAUTH
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    
    # 'corsheaders.middleware.CorsMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'tech_investement.urls'

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
                # `allauth` needs this from django
                'django.template.context_processors.request',
            ],
        },
    },
]

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'github': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': 'Ov23liHk3KGtUB5OBn8g',
            'secret': '783a02e3eb1288296ce7ba2aa977e56ad1d5b5f7',
            'key': ''
        }
    }
}

WSGI_APPLICATION = 'tech_investement.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

#####################sqlite####################
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
#####################end sqlite####################


############### mysql ################
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'codius',
#         'USER': 'peekay',
#         'PASSWORD': 'kali',
#         'HOST': '54.237.50.146',   # Or the hostname where your MySQL server is running
#         'PORT': '3306',        # Default MySQL port
#     }
# }

#####################end mysql####################

############### postgress ################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'HmrcGSSYeHgGQjepqPXXKkChTXGjNgXM',
        'HOST': 'viaduct.proxy.rlwy.net',   # Or the hostname where your MySQL server is running
        'PORT': '38610',        # Default MySQL port
    }
}

#####################end postgress####################

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,
        }
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# STATIC_URL = 'http://54.237.50.146/codius-static/'

STATIC_URL = '~/tech_investement/investor/static/'
STATIC_ROOT = '~/tech-investment/tech_investement/investor/static'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#smtp config
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'mikenjanja7@gmail.com'
EMAIL_HOST_PASSWORD = '0723534084@Jackline'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
DEFAULT_FROM_EMAIL = ''


