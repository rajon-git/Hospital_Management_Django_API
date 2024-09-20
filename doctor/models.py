from django.db import models

# Create your models here.
class Specialization(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=40)

    def __str__(self):
        return self.name

class Designation(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=40)

    def __str__(self):
        return self.name

class AvailabelTime(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name