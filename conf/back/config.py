from .common import *

PUBLIC_REGISTER_ENABLED = True
DEBUG = False
TEMPLATE_DEBUG = False

SECRET_KEY = 'e6V3ZVq4no'

MEDIA_URL = "http://192.168.56.112/media/"
STATIC_URL = "http://192.168.56.112/static/"
ADMIN_MEDIA_PREFIX = "http://192.168.56.112/static/admin/"
SITES["api"]["scheme"] = "http"
SITES["api"]["domain"] = "192.168.56.112"
SITES["front"]["scheme"] = "http"
SITES["front"]["domain"] = "192.168.56.112"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "taiga",
        "HOST": "db",
        "USER": "postgres",
        "PASSWORD": "AzHSuhXO3h"
    }
}

#DEFAULT_FROM_EMAIL = "john@doe.com"
#CHANGE_NOTIFICATIONS_MIN_INTERVAL = 300 #seconds
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_USE_TLS = False
#EMAIL_USE_SSL = False # You cannot use both (TLS and SSL) at the same time!
#EMAIL_HOST = 'localhost'
#EMAIL_PORT = 25
#EMAIL_HOST_USER = 'user'
#EMAIL_HOST_PASSWORD = 'password'

EVENTS_PUSH_BACKEND = "taiga.events.backends.rabbitmq.EventsPushBackend"
EVENTS_PUSH_BACKEND_OPTIONS = {"url": "amqp://taiga:oMNDNkM4WC@rabbit:5672/taiga"}

CELERY_ENABLED = True
