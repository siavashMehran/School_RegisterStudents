from django.db import models
import random
from django.db.models.signals import pre_save
# Create your models here.


class MyBaseUser(models.Model):

    melli_code      = models.PositiveIntegerField('کد ملی', unique=True, max_length=10, blank=False)
    phone           = models.PositiveIntegerField('تلفن', unique=True, max_length=11, blank=False)
    two_factor_code = models.PositiveIntegerField('کد رهگیری', max_length=10, blank=True, null=True)


    def __str__(self):
        return str(self.melli_code)

    

def pre_save_reciever(sender, instance, *args, **kwargs):

    instance.two_factor_code = random.randint(10000, 99999)

pre_save.connect(receiver=pre_save_reciever, sender=MyBaseUser)

