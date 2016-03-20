from django.db import models

from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, related_name='author')
    likes = models.ManyToManyField(User, related_name='likes')


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)


class Author(models.Model):
    rating = models.IntegerField()
    name = models.CharField(max_length=50)


class Article(models.Model):
    author = models.ForeignKey(Author)
    text = models.TextField()