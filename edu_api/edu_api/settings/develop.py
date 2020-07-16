"""
Django settings for edu_api project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
import datetime
import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, os.path.join(BASE_DIR, "apps"))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '11&j5*12$r6u#$lsr!o1km8yr5yd+0#&d8jm$=zvgwa#l@1v9v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['api.baizhishop.com', 'www.baizhishop.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',

    # x admin配置
    'xadmin',
    'crispy_forms',
    'reversion',
    'django_filters',

    # 富文本编辑器配置
    'ckeditor',  # 富文本编辑器
    'ckeditor_uploader',  # 富文本编辑器的上传模块

    'home',
    'users',
    'course',
    'cart',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'edu_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '../../templates')]
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

WSGI_APPLICATION = 'edu_api.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bz_edu',
        'HOST': "localhost",
        'USER': "root",
        "PASSWORD": '123456',
        "PORT": 3306,
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# 允许跨域请求
CORS_ORIGIN_ALLOW_ALL = True

# 项目的日志配置
LOGGING = {
    # 版本
    'version': 1,
    # 是否禁用已存在的日志器
    'disable_existing_loggers': False,
    # 格式化日志信息
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    # 日志的过滤信息
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    # 处理日志的方法
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {
            # 记录到文件中的日志等级
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            # 日志位置  日志的文件名  日志的保存目录
            'filename': os.path.join(os.path.dirname(BASE_DIR), "logs/lesson_api.log"),
            # 日志文件的大小  100M
            'maxBytes': 100 * 1024 * 1024,
            # 日志文件的最大数量
            'backupCount': 10,
            # 日志的格式
            'formatter': 'verbose'
        },
    },
    # 日志对象，与django集成使用
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'propagate': True,  # 是否让日志信息继续冒泡给其他的日志处理系统
        },
    }
}

# DRF 默认配置
REST_FRAMEWORK = {
    # 全局异常配置
    "EXCEPTION_HANDLER": "utils.exceptions.exception_handler",
    # 添加认证方式
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
}

AUTH_USER_MODEL = 'users.UserInfo'

# jwt配置
JWT_AUTH = {
    # 有效时间
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=30000 * 60),
    # 自定义jwt返回值的格式方法
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'users.utils.jwt_response_payload_handler',
}

# 自定义多条件登录
AUTHENTICATION_BACKENDS = [
    'users.utils.UserAuthBackend',
]

# django 连接redis设置

CACHES = {
    # 默认库
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        # 连接的redis所在服务的端口以及ip
        "LOCATION": "redis://127.0.0.1:6379/0",
        # 使用客户端的方式
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },

    # 验证码储存位置
    "sms_code": {
        "BACKEND": "django_redis.cache.RedisCache",
        # 连接的redis所在服务的端口以及ip
        "LOCATION": "redis://127.0.0.1:6379/10",
        # 使用客户端的方式
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # 购物车的储存位置
    "cart": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/9",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# 编辑器的配置
KEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',  # 展示哪些工具栏
        'height': 300,  # 编辑器的高度
        'width': 300,
    },
    # 'default': {
    #     'toolbar': 'Custom',
    #     'toolbar_Custom': [
    #         ['Bold', 'Italic', 'Underline'],
    #         ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter',
    #          'JustifyRight', 'JustifyBlock', "image"],
    #         ['Link', 'Unlink'],
    #         ['RemoveFormat', 'Source']
    #     ]
    # }
}

# 富文本上传图片的路径  为空的话代表使用django的文件上传
CKEDITOR_UPLOAD_PATH = ''
