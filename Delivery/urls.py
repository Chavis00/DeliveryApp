from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "delivery"
urlpatterns = [
    path('', views.index, name='index'),    
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('restaurant/<int:restaurant_id>', views.restaurant, name="restaurant"),

    path('add/<int:id>/', views.addProduct, name="add"),
    path('delete/<int:id>/', views.deleteProduct, name="delete"),
    path('substract/<int:id>/', views.substractProduct, name="substract"),
    path('clean/', views.cleanCart, name="clean"),

]
