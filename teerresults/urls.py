from django.urls import path
from teerresults import views

urlpatterns = [
    path('teerhome/', views.teerhome, name='teerhome')
]
