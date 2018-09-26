from django.urls import path

from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('toto/<int:cid>', views.detail, name='detail'),
    path('edit/<int:pers_id>', views.edit, name='edite'),
]