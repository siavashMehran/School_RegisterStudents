from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

class User_Auth_State(models.Model):

    user = models.OneToOneField(to=get_user_model(), on_delete=models.CASCADE)

    is_good = models.BooleanField(default=False)