"""
Django settings for workspace project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os.path
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-fqrt8pb0$&!l20k8$8(+fx7zg&d@u59ja5q-1lr(ac+*ik4#z)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']



# Application definition

INSTALLED_APPS = [
    'neulhaerang_review',
    'static_app',
    'member',
    'admin',
    'main',
    'customer_center',
    'mypage',
    'neulhajang',
    'neulhaerang',
    'notice',
    'search',
    'workspace',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'workspace.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'workspace.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


DATABASES = {
    "default": {
        # MySQL 모듈 경로
        "ENGINE": "django.db.backends.mysql",
        # DATABASE 이름
        "NAME": "django",
        # 계정 이름
        "USER": "Giboo",
        # 비밀번호
        "PASSWORD": "1234",
        # MySQL 서버가 실행 중인 서버 IP 또는 도메인
        # "HOST": "127.0.0.1",
        "HOST": "43.203.16.105",
        # 포트번호
        "PORT": "3306"
    }
}



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = False


# {% static '경로' %}로 사용하면 경로 앞에 /static을 붙인다.
STATIC_URL = 'static/'
# /static으로 요청이 들어오면 실제 static 경로를 찾아준다.
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

# 파일 접근 시
MEDIA_URL = '/upload/'

# 파일 업로드 시
MEDIA_ROOT = os.path.join(BASE_DIR, 'upload')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = 'service.center.12342@gmail.com'
EMAIL_HOST_PASSWORD = 'sikltcmonprcmfdm'

# CORS 설정 추가
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # 허용하려는 클라이언트 주소 (React 앱 주소)
]