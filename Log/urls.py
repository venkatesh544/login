from django.core import paginator
from django.urls import path

from Log import views

urlpatterns = [
    path('',views.home,name='home'),
    path('loginpage', views.Loginpage,name='loginpage' ),
    path('BDAloginpage', views.ABDAloginpage, name='BDAloginpage'),
    path('Dashboard', views.DDashboard, name='Dashboard'),
    path('upload/', views.Upload, name='upload'),
    path('Books/', views.BBooks, name='Books'),
  #  path('search', views.Search, name='search'),
    path('delete/<int:pk>/', views.Delete, name='delete'),

]