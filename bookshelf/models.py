from django.db import models
from django.contrib.auth.models import User  

class Book(models.Model):
    PRIVACY_CHOICES = [
        ('public', 'Public'),
        ('private', 'Private'),
    ]
    title = models.CharField(max_length=510)
    author = models.CharField(max_length=255)
    addedby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    privacy = models.CharField(max_length=7, choices=PRIVACY_CHOICES, default='public')
    image = models.ImageField(upload_to='book_images/', blank=True, null=True) 

    def __str__(self):
        return self.title
class UserImage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Image"
    
    # def save(self, *args, **kwargs):
    #     if not self.image:
    #         self.image = 'default_user_image.jpg'  # Set a default image if none is provided
    #     super().save(*args, **kwargs)  # Call the original save method