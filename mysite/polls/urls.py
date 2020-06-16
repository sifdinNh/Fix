from django.urls import path
from . import views, views2
urlpatterns = [
    path('', views.index, name='views1'),
    path('v2/', views2.index, name='views2'),
]