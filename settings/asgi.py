# ASGI
from django.core.asgi import get_asgi_application
import os

# MAIN
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.config")
application = get_asgi_application()
