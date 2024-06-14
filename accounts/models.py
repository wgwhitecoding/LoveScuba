from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    age = models.IntegerField(blank=True, null=True)
    country_of_origin = CountryField(blank=True, null=True)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    DIVER_TYPE_CHOICES = [
        ('leisure', 'Leisure'),
        ('professional', 'Professional'),
    ]
    diver_type = models.CharField(max_length=12, choices=DIVER_TYPE_CHOICES, blank=True, null=True)
    is_professional = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
