from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class Action(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    verb = models.CharField(max_length=100)
    target_ct = models.ForeignKey(ContentType, blank=True, null=True, on_delete=CASCADE)
    target_id = models.PositiveIntegerField(blank=True, null=True)
    target = GenericForeignKey('target_ct','target_id')
    created = models.DateTimeField(auto_now_add=True)