from django.urls import path
from . import views 

urlpatterns =[
    path('', views.home, name='home'),
    path('login/',views.officer_login, name= 'login'),
    path('forget/',views.forget, name = 'forget'),
    path('register/', views.register, name = 'register'),
    path('Government_dashboard/', views.dashboard,name='Government_dashboard'),
]