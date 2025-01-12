from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='polls/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='polls/logout.html'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_habit, name='create_habit'),
    path('list/', views.habit_list, name='habit_list'),
    path('update/<int:habit_id>/', views.update_habit, name='update_habit'),
    path('delete/<int:habit_id>/', views.delete_habit, name='delete_habit'),
    path('habit/<int:habit_id>/progress/', views.habit_progress, name='habit_progress'),
    path('habit/<int:habit_id>/progress/add/', views.add_progress, name='add_progress'),
]

