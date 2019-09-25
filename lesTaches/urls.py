from django.urls import path

from . import views

urlpatterns = [
    path('home/<param>', views.home, name='home'),
    path('listing', views.task_listing, name='listing')
]