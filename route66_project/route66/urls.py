from django.urls import path

from . import views
# Paths to the 3 routes I have made
urlpatterns = [
# KEY: make sure named routes are unique!
    path('', views.index, name='index'),
    path('gogetthegood/', views.gogetthegood, name='index'),
    path('happyhappyjoyjoy/', views.happyhappyjoyjoy, name='index'),
    path('whydidntyoubelieveme/', views.whydidntyoubelieveme, name='index'),
]