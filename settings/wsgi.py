# WSGI
from django.core.wsgi import get_wsgi_application
import os

# MAIN
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.config")
application = get_wsgi_application()
app = application