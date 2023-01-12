from django.urls import path

from .views import hello_world , new_india


urlpatterns = [path("", hello_world),path("new/",new_india)]







