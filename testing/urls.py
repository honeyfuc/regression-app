from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("upload", views.upload_file, name="upload_file"),
    path("hello", views.hello, name="hello"),
    path("rest", views.rest, name="rest"),
    path('table', views.table, name='table')
]