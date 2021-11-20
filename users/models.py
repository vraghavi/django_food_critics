from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from django.core.validators import MaxValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    points = models.IntegerField(validators=[MaxValueValidator(5000)],blank=False, default=0)
    mobileno = models.BigIntegerField(validators=[MaxValueValidator(9999999999)],blank=True, null=True)
    role = models.CharField(default="regular",max_length=50)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()