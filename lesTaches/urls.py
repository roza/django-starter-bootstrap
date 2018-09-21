from django.urls import path

from . import views

urlpatterns = [
    path(r'home/<param>', views.home, name='home'),
    path(r'listing', views.task_listing, name='listing')
]