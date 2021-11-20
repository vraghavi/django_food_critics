from django.urls import path
from . import views
app_name = 'users'
urlpatterns = [
    # path('',views.home, name='home'),
    # path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile/<str:username>', views.user_profile, name='profile'),
    path('user-points', views.user_points, name='user-points'),
    path('update-profile',views.update_profile, name='update-profile')
]
    