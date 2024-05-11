from django.db import models
from django.contrib.auth.models import User
from genres.models import *
from Auth.models import *
# Create your models here.

class Novel(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(
        UserCustom, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.FileField(null=True, blank=True, upload_to="Novel",
                              default='/Novel/default.png')
    genres = models.ManyToManyField(
        Genres, related_name='manga_genres', blank=True)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=200, null=True,choices=[('continue', 'tiếp tục'),('stoped', 'Đã dừng lại'), ('complete', 'Hoàn thành')] ,blank=True)
    features = models.CharField(max_length=200, null=True,choices=[('hot', 'Hot'),('new', 'New'), ('full', 'Full')] ,blank=True)
    views = models.IntegerField(null=True, blank=True, default=0)
    rating = models.FloatField(null=True, blank=True, default=0)
    favorites = models.IntegerField(null=True, blank=True, default=0)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    id = models.BigAutoField(primary_key=True)
    novel = models.ForeignKey(Novel, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(UserCustom, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.rating)
