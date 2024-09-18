from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    author = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2 , max_digits=5)

    def __str__(self):
        return self.title
