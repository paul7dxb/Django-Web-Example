from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    #One to one relationship with User Acccount. CASCADE will delete profile on user deletion. Not other way around
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    # Profile picture. Choose default image and directory where profile pictures are stored
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    # Dunder STR method for printing out object
    def __str__(self) -> str:
        return f'{self.user.username} Profile'