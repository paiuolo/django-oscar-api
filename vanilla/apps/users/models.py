from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
import os


class Profile(models.Model):
    USER = 1
    AUTHOR = 2
    ADMIN = 3
    ROLE_CHOICES = (
        (USER, 'User'),
        (AUTHOR, 'Author'),
        (ADMIN, 'Admin'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)
    
    location = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    
    date_updated = models.DateTimeField(_('Date updated'), auto_now_add=True)
    name = models.CharField(_('Name'), null=True, blank=True, max_length=128)
    surname = models.CharField(_('Surname'), null=True, blank=True, max_length=128)
    description = models.TextField(_('Description'), null=True, blank=True)
    
    slug = models.SlugField(_('Slug'), max_length=128, unique=True, blank=True)
    image = models.ImageField(upload_to=os.path.join('images', 'series'), blank=True, null=True)
    
    is_public = models.BooleanField(_('Show on site'), default=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()