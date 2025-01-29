
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_email_verified = models.BooleanField(default=False)
    mobile_no = models.CharField(max_length=15, unique=True, blank=True, null=True)

    def __str__(self):
        return self.username
    
