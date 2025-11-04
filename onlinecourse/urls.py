from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homepage, name='home'),
    path('login/',views.login_user,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('quizpro/', views.quizpro, name='quizpro'),
    path('register/', views.register, name='register'),
    path('courses/', views.browserpage, name='browserpage'),
    path('admin/',admin.site.urls,),
    path('fullstack/',views.fullstack,name='fullstack'),
    path('datascience/',views.datascience,name='datascience'),
    path('reactjs/',views.reactjs,name='reactjs'),
    path('java/',views.java,name='java'),
    path('cloud/',views.cloud,name='cloud'),
    path('cprogramming/',views.cprogramming,name='cprogramming'),
    path('cyber/',views.cybersecurity,name='cybersecurity'),
    path('excel/',views.excel,name='excel'),
    path('logout/',views.logout_view,name='logout'),
    path('about/',views.about,name='about'),

    # Start button (C1 page)
    path('c1/', views.c1_page, name='c1_page'),
    path('j1/',views.j1_page,name='j1_page'),
    path('r1/',views.r1_page,name='r1_page'),

]

    






   

  


