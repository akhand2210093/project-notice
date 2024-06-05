from django.db import models
from user.models import User
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField


def validate_file_size(value):
    filesize = value.size
    
    # Limit size to 5MB
    limit_mb = 1
    limit = limit_mb * 1024 * 1024
    if filesize > limit:
        raise ValidationError(f"File size should not exceed {limit_mb} MB.")
    
class Document(models.Model):
    editor = models.ForeignKey(User, on_delete=models.CASCADE)
    pdf = CloudinaryField(resource_type='raw', folder='documents', validators=[validate_file_size])
    file_title = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_title