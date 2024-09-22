from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    author = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2 , max_digits=5)
    cover = models.ImageField(upload_to='covers/' , blank=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail' , args=[self.id])

class Comment(models.Model):
    user = models.ForeignKey(get_user_model() , on_delete=models.CASCADE)
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book , on_delete=models.CASCADE)

    def __str__(self):
        return self.text






