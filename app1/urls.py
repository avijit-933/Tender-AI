from django.contrib import admin
from django.urls import path, include
from app1 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
<<<<<<< HEAD
    path('login/', views.officer_login, name='login'),
    path('forget/', views.forget, name='forget'),
    path('register/', views.register, name='register'),
    #path('Government_dashboard/', views.Government_dashboard, name='Government_dashboard'),
    path('Companydashboard/', views.Companydashboard, name='Companydashboard'),
    path('browse_tenders/', views.browse_tenders, name='browse_tenders'),
    path('submit_bid/', views.submit_bid, name='submit_bid'),
    path('submission_status/', views.submission_status, name='submission_status'),
    path('watch_tenders/', views.watch_tenders, name='watch_tenders'),
    path('logout/', views.logout, name='logout'),
    #path('evaluationdashboard/',views.evaluationdashboard,name='evaluationdashboard'),
      # Note: underscore, not hyphen
=======
    path('login/',views.officer_login, name= 'login'),
    path('forget/',views.forget, name = 'forget'),
    path('register/', views.register, name = 'register'),
    path('Government_dashboard/', views.dashboard,name='Government_dashboard'),
    path('createtender/', views.createtender, name = 'createtender'),
    path('evaluation/', views.evaluation, name = 'evaluation'),
    path('managetender/', views.managetender, name = 'managetender'),

>>>>>>> 6ce756ec68e4d34644e87f345cd038b0aa849ae4
]