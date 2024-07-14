# URLS
from django.urls import path
from . import views

# MAIN
urlpatterns = [
    path(route="", view=views.home, name="home"),
    path(route="ethereum/<int:strength>/", view=views.ethereum, name="ethereum")
]
