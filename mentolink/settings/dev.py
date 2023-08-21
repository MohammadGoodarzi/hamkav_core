from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-qdg4$^=t9$)5m*6)44-*kzj^sqtgg^zv1r(in&(#&2%1j58qdm"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]
CORS_ORIGIN_ALLOW_ALL = True



EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


INSTALLED_APPS = INSTALLED_APPS + [
    "debug_toolbar",  #https://django-debug-toolbar.readthedocs.io/
    
]

MIDDLEWARE = MIDDLEWARE + [
    "debug_toolbar.middleware.DebugToolbarMiddleware", #django-debug-toolbar
    
]

INTERNAL_IPS = [  # django-debug-toolbar
    # ...
    "127.0.0.1",
    # ...
]





if DEBUG:   #django-debug-toolbar in docker implementation
    import socket  # only if you haven't already imported this
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]



try:
    from .local import *
except ImportError:
    pass




