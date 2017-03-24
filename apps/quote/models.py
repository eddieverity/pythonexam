from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
  name=models.CharField(max_length=64)
  alias=models.CharField(max_length=64)
  email=models.CharField(max_length=64)
  password=models.CharField(max_length=512)
  date_of_birth=models.DateField(auto_now=False, auto_now_add=False)
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)

class Quote(models.Model):
  description=models.CharField(max_length=256)
  quoted_by=models.CharField(max_length=64)
  poster=models.ForeignKey(User, related_name='user_posts')
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)

class Favorite(models.Model):
  quote_favorite=models.ForeignKey(Quote, related_name='quote_fav')
  user_favorite=models.ForeignKey(User, related_name='users_fav')
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)