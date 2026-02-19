from django.contrib import admin
from django.urls import path, include
from app1 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/',views.officer_login, name= 'login'),
    path('forget/',views.forget, name = 'forget'),
    path('register/', views.register, name = 'register'),
    path('Government_dashboard/', views.dashboard,name='Government_dashboard'),
    path('createtender/', views.createtender, name = 'createtender'),
    path('evaluation/', views.evaluation, name = 'evaluation'),
    path('managetender/', views.managetender, name = 'managetender'),
     path('browse_tenders/', views.browse_tenders, name = 'browse_tenders'),
      path('submit_bid/', views.submit_bid, name = 'submit_bid'),
       path('track_submissions/', views.track_submissions, name = 'track_submissions'),
        path('watchedtenders/', views.watchedtenders, name = 'watchedtenders'),
    

]