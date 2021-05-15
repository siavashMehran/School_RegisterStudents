
from django.core.exceptions import ValidationError
from django.db import models
import random
from django.db.models.signals import pre_save



class MyBaseUser(models.Model):

    melli_code      = models.CharField('کد ملی', unique=True, max_length=10, blank=False)
    phone           = models.CharField('تلفن', unique=True, max_length=11, blank=False)
    two_factor_code = models.CharField('کد رهگیری', max_length=10, blank=True, null=True)

    is_good_to_go   = models.BooleanField(default=False)
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.melli_code)

    def clean_melli_code(self):
        if len(self.melli_code) < 10:
            return ValidationError('melli code wrong')
        return self.melli_code


def pre_save_reciever(sender, instance, *args, **kwargs):
    
    if not instance.two_factor_code :
        instance.two_factor_code = random.randint(10000, 99999)
        print(instance.two_factor_code)


pre_save.connect(receiver=pre_save_reciever, sender=MyBaseUser)

