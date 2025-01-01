from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #if user is deleted , delete its profile but not vice versa
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')


    def __str__(self):
        return f'{self.user.username} Profile'
    
# resizing image to optimise the image resolution
    # def save(self, *args, **kawrgs):
        
    #     # method to accept any positional (*args) or keyword arguments (**kwargs) passed to it.
    #     super().save(*args, **kawrgs) 

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

