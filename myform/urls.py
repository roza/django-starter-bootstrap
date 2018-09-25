from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.contact, name='contact')
]