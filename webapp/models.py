import os
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ContactInfo(models.Model):
    '''Manages the contact form/page'''
    name = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        error_messages={'required': ("Provide a first and last name.")})
    
    email = models.EmailField(
        null=True,
        blank=True,
        error_messages={'required': ("Provide an email address.")})
    
    phone = models.CharField(max_length=9,
                             null=False,
                             blank=False,
                             error_messages={'required':("Provide a valid phone number")})
    
    message = models.TextField(
        null=False,
        blank=False,
        error_messages={'required': ("You must say something.")})

    def __str__(self):
        return self.name + ' ' + self.email
    

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profiles/', null=True, blank=True)
    phone = models.CharField(max_length = 9, null=True, blank=True, default='Not provided')
    about = models.TextField(null=True, blank=True, default='Not provided')
    vehiculated = models.BooleanField(null=True, blank=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = os.path.join('../static/img/avatar.png')
        return url

    def __str__(self):
        return str(self.user)