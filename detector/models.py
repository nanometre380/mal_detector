from django.db import models

# Create your models here.
class Black(models.Model):
    black_id = models.CharField(max_length = 100)
    url = models.CharField(max_length = 500)

    def __str__ (self):
        return self.black_id

class White(models.Model):
    url = models.CharField(max_length=500)
