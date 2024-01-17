from django.db import models
from django.contrib.auth.models import User

class Plant(models.Model):
  name = models.CharField(max_length = 255)
  scientific_name = models.CharField(max_length = 255)
  image = models.ImageField(upload_to='plant_image')
  description = models.CharField(max_length = 1000)
  Mostly_caused_disease_name = models.CharField(max_length = 255)
  disease_image = models.ImageField(upload_to='disease_image')
  solution = models.CharField(max_length = 255)

  def __str__(self):
    return self.name
  

class UserPlant(models.Model):
  name = models.CharField(max_length = 255)
  image = models.ImageField(upload_to='user_disease_image')
  description = models.CharField(max_length = 255)
  created_by = models.ForeignKey(User, on_delete = models.CASCADE)
  created_at = models.DateTimeField(auto_now = True)

  def __str__(self):
    return self.name

class UserSuggestion(models.Model):
    plant = models.ForeignKey(UserPlant, on_delete = models.CASCADE)
    suggestion = models.CharField(max_length = 255)
    given_by = models.ForeignKey(User, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now = True)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

    def __str__(self):
      return str(self.given_by)
    
class Mark(models.Model):
    user_plant = models.ForeignKey('UserPlant', on_delete = models.CASCADE)
    suggestion = models.ForeignKey('UserSuggestion', on_delete = models.CASCADE)
    likes = models.ManyToManyField(User, related_name='post', blank=True)
    created_at = models.DateTimeField(auto_now = True)

    def __str__(self):
       return self.user_plant.created_by
    
class DailyUpdates(models.Model):
    name = models.CharField(max_length = 255)
    image = models.ImageField(upload_to="daily_updates")
    description = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now = True)
    created_by = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
       return str(self.name)