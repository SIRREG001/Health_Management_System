from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=500)
    username = models.CharField(max_length=500, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        email_username, email_domain = self.email.split("@")
        if self.usernname == "" or self.username == None:
            self.username = email_username

        super(User, self).save(*args, **kwargs)


