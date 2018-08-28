from django.urls import path

from . import views

urlpatterns = [
	path('', views.index),
	path('register/', views.register), # Register a new user 
	path('login/', views.login), # Login a user
	path('logout/', views.logout), # Logout a user
	path('reset_password_email/', views.reset_password_email), # Reset password email
	path('password_reset/', views.password_reset), # Reset user password 
	path('user_data_get/', views.user_data_get), # Get data from a LOGGED IN user
	path('user_data_set/', views.user_data_set), # Set data for a LOGGED IN user
	path('tools_search_1/', views.tools_search_1), # Search tools from sidebar
]