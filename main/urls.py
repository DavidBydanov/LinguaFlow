"""URL-маршруты для приложения main"""
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-card/', views.add_card, name='add_card'),
    path('add-grammar/', views.add_grammar, name='add_grammar'),
    path('training/', views.start_training, name='training'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
