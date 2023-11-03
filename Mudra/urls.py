from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='mudra-home'),
    path('signup/', views.signup, name='mudra-signup'),
    path('login/', views.login, name='mudra-login'),
]