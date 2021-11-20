from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse

# Create your models here.

class Comments(models.Model):
    date_commented = models.DateTimeField(auto_now_add=True)
    user_commented = models.TextField(blank=False)
    description = models.TextField(blank=False)
    blog = models.ForeignKey('FoodBlog', on_delete=models.CASCADE, related_name='blog')
    def __str__(self):
        return self.description
    
    def get_absolute_url(self):
        return reverse('food_critics:blog-in-detail',args=[self.blog.id])

class FoodBlog(models.Model):
    points = models.IntegerField(default=0)
    image = models.TextField(blank=True)
    title = models.TextField(blank=False)
    short_description = models.TextField(blank=False)
    detail_description = models.TextField(blank=False)
    no_of_comments = models.PositiveSmallIntegerField(blank=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    user_posted = models.TextField(blank=False)

    def __str__(self):
        return self.title

class BlogDetailView:
    def __init__(self, blog, comments):
        self.blog = blog
        self.comments = comments




