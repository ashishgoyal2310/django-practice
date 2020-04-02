from django.urls import path
from teerresults import views

urlpatterns = [
    path('', views.teerhome, name='teerhome'),
    path('dreamnumber/', views.dreamnumber, name='dreamnumber'),
    path('resultlist/', views.resultlist, name='resultlist'),
    path('commonnumber/', views.commonnumber, name='commonnumber'),
]
