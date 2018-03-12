from django.db import models

# Create your models here.
class info(models.Model):
    version = models.DecimalField(max_digits=2, decimal_places=1, default=1.1)
    description = models.CharField(max_length=50, default='This is test app for awsome MYOB')
    lastcommitsha = models.CharField(max_length=50, default='default')

    def __str__(self):
        return self.description
