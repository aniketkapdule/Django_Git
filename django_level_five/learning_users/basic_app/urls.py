from django import path, include
from basic_app import views

#template urls

app_name = basic_app

urlpatterns = [
    path('register/', views.register, name='register')
]