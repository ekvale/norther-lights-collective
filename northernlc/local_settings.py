# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_z@1tatsj^vxh@b^$oh)o-ged@_1(%2na)0(r$@+^h!p$mkk@w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['www.northern-lights-collective.com', 'northern-lights-collective.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'btre_prod',
        'USER': 'dbadmin',
        'PASSWORD': 'Atheism!2828',
        'PORT': '5432',
        'HOST': 'localhost'
    }
}

# Email settings
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.your-email-provider.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'your-email@example.com'
# EMAIL_HOST_PASSWORD = 'your-email-password'
