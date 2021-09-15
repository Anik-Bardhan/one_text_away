from django.contrib import admin
from django.urls import path,include
from blog import views
urlpatterns = [
    path('',views.index,name="index"),
    path('write/',views.write,name="write"),
    path('<slug:slug>/',views.post_detail,name='post_detail'),
]