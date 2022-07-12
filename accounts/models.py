import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.utils import CustomUserManager

# Create your models here.


class Account(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    is_worker = models.BooleanField()
    username = None

    REQUIRED_FIELDS = ["name", "birth_date"]
    USERNAME_FIELD = "email"
    objects = CustomUserManager()
