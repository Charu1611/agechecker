from django.urls import path
from . import views
urlpatterns = [
    path('result',views.index, name="index"),
     path('',views.search, name="search"),
]