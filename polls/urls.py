from django.urls import path
from polls import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add, name='add')
]
