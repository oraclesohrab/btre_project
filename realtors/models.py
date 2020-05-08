from django.db import models
from datetime import datetime
from django.core.validators import RegexValidator
# Create your models here.


class Realtor(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone_validator = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(
        validators=[phone_validator], max_length=17, blank=True)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
