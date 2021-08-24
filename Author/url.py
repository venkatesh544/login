from django.urls import path
from Author import views

app_name:'Author'

urlpatterns = [
    path('house', views.House, name='house'),
    path('Ather_Book', views.AAther_Book, name='Ather_Book'),
    path('Ather_Log', views.AAther_Log, name='Ather_Log'),
    path('Ather_Books_store', views.AAther_Book_store, name='Ather_Books_store'),
    path('loginpage', views.Loginpage, name='loginpage'),

]