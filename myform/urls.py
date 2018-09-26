from django.urls import path

from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('detail/<int:cid>', views.detail, name='detail'),
    path('edit/<int:pers_id>', views.edit, name='edite'),
    path('list', views.liste, name='listing')
]