from django.urls import path

from . import views

app_name = "loaders"

urlpatterns = [
    path('', views.home, name='home'),
    path("kaggle/", views.upload_files, name="upload_files"),
]
