from django.urls import path
from . import views

app_name = "onlinestore"

urlpatterns = [
    path("uacraft-be.vercel.app/", views.main, name="main"),
]
