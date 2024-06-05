from django.db import models
from cloudinary.models import CloudinaryField
from user.models import User

class Event(models.Model):
    coordinator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=127, unique= True, blank = False)
    society_name = models.CharField(max_length=127, blank = False)
    description = models.TextField(blank = False)
    date = models.DateField()
    time = models.TimeField()
    place = models.CharField(max_length=255)
    flex_image = CloudinaryField('image', folder='flex_images')

    def __str__(self):
        return self.title
