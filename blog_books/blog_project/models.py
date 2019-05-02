from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    RATING = (
        ('1', '1점'),
        ('2', '2점'),
        ('3', '3점'),
        ('4', '4점'),
        ('5', '5점'),
    )
    title = models.CharField(max_length=200)
    review = models.TextField()
    price = models.CharField(max_length=20)
    score = models.CharField(max_length=1, choices=RATING)

    def __str__(self):
        return self.title   

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()