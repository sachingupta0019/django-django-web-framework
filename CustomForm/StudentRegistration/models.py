from django.db import models

# Create your models here.
class enrollDB(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=20)
    rpassword = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name