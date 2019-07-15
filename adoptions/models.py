from django.db import models

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=15)
    breed = models.CharField(max_length=30, blank=True)
    sex = models.CharField(max_length=1, choices=[('M','Male'),('F','Female')], blank=True)
    age = models.IntegerField(null=True)
    submitter = models.CharField(max_length=100)
    submission_date = models.DateTimeField()
    description = models.TextField(blank=True)
    vaccinations = models.ManyToManyField('Vaccine', blank=True) # Foreign key to Vaccine model
    picture = models.URLField(blank=True)
    def __str__(self):
        return self.name

class Vaccine(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name
