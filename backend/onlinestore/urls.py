from django.urls import path
from . import views

app_name = "onlinestore"

urlpatterns = [
    path("", views.main, name="main"),
]
