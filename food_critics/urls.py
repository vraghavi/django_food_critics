from django.urls import path
from . import views
app_name = 'food_critics'
urlpatterns = [
    path('',views.home, name='home'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('search', views.search, name='search'),
    path('blogs',views.blog_list, name='blog-list'),
    path('<int:blog_id>', views.blog_in_detail, name='blog-in-detail'),
    path('newcomment', views.newcomment, name='new-comment'),
    path('editcomment', views.editcomment, name='edit-comment'),
    path('deletecomment', views.deletecomment, name='delete-comment')
]
    