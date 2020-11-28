from django.db import models

# Create your models here.

class Friend(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name