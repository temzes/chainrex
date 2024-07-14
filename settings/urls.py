# URLS
from django.urls import path, include

# MAIN
urlpatterns = [
    path(route="", view=include("application.application.urls"), name="application"),
]
