from django.db import models
from user_entity.models import User

# Create your models here.

class AdminEntity(User):
    departmentRole = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.username}"
    