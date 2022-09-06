from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class UserLevels(models.TextChoices):
    IS_CRITIC_BOL = True
    NOT_CRITIC_BOL = False

class UserManager(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=127, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    bio = models.TextField(null=True)
    is_critic = models.CharField(max_length=10, null=True, choices=UserLevels.choices, default=UserLevels.NOT_CRITIC_BOL)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'birthdate']