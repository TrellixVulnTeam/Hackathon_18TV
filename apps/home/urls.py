# -*- encoding: utf-8 -*-

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.tests, name='home'),
    path('first', views.first, name='first'),


    # Matches any html file

    path('profile.html',views.profile,name='profile'),
    path('diets.html',views.diets,name='diets'),
    #path('tests.html',views.tests,name='tests'),
    path('searched',views.searched,name='searched'),
    path('hairloss.html',views.hair, name="hairloss"),
    path('weight.html',views.weight, name="weight"),
    path('skin.html',views.skin, name="skin"),
    path('nutrition.html',views.nutrition, name="nutrition"),
    path('depression.html',views.depression, name="depression"),
    path('sleepdisorders.html',views.sleepdisorders, name="sleepdisorders"),
    path('weightmanagement.html',views.weightmanagement, name="weightmanagement"),
    path('workholic.html',views.workholic, name="workholic")

]
