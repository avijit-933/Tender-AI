from django.contrib import admin
from django.urls import path, include
from app1 import views


urlpatterns = [

    path('', views.home, name='home'),

    path('login/', views.officer_login, name='login'),
    path('login_view/', views.login_view, name='login_view'),
    path('forget/', views.forget, name='forget'),
    path('register/', views.register, name='register'),
    path('bidder_register/', views.bidder_register, name='bidder_register'),
    #path('Government_dashboard/', views.Government_dashboard, name='Government_dashboard'),
    
    #path('evaluationdashboard/',views.evaluationdashboard,name='evaluationdashboard'),
      # Note: underscore, not hyphen

    
    
    
    path('Government_dashboard/', views.dashboard,name='Government_dashboard'),
    path('createtender/', views.createtender, name = 'createtender'),
    path('evaluation/', views.evaluation, name = 'evaluation'),
    path('managetender/', views.managetender, name = 'managetender'),



]