from django.urls import path
from . import views
app_name = 'food_critics'
urlpatterns = [
    path('',views.home, name='home'),
    path('search', views.search, name='search'),
    path('sort-by-date', views.sort_by_date, name='sort-by-date'),
    path('blogs',views.blog_list, name='blog-list'),
    path('<int:blog_id>', views.blog_in_detail, name='blog-in-detail'),
    path('newcomment', views.newcomment, name='new-comment'),
    path('editcomment', views.editcomment, name='edit-comment'),
    path('deletecomment', views.deletecomment, name='delete-comment'),
    path('edit-points', views.edit_points, name='edit-points')
]
    