import os
from pathlib import Path

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Configuración de desarrollo (No usar en producción)
SECRET_KEY = 'django-insecure-dk351^sjdp9ue!d_b2tyb6s18cuy5hs%qcmmj1*r)yh0u#hy9b'
DEBUG = True
ALLOWED_HOSTS = []

# Aplicaciones instaladas en el ecosistema
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Librerías de terceros instaladas
    'rest_framework',
    'corsheaders',
    # Nuestra aplicación local
    'empleados',
]

# Control de flujos de peticiones (Middlewares)
MIDDLEWARE = [
    # CorsMiddleware DEBE ir lo más arriba posible, indispensablemente antes de SecurityMiddleware
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'rh_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'rh_django.wsgi.application'

# Configuración de Conexión a la Base de Datos MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'recursos_humanos_db',
        'USER': 'root',
        'PASSWORD': 'Superheaven22',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# Validación de contraseñas por defecto
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Configuración de idioma y zona horaria
LANGUAGE_CODE = 'es-co'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CONFIGURACIÓN CORS ESTRICTA
# Se habilitan únicamente las direcciones locales de Angular y React (Vite)
CORS_ALLOWED_ORIGINS = [
    'http://localhost:4200',
    'http://localhost:5173',
]