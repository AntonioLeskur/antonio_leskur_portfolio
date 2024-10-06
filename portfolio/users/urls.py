from django.urls import path
from . import views


urlpatterns = [
	path('users/register/', views.register_user, name='register'),
    path('users/login/', views.login_user, name='login'),
    path('users/logout/', views.logout_user, name='logout'),
]