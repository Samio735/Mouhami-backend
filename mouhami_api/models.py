from django.db import models

# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=255, unique=True,primary_key=True)
    
class Specialities(models.Model):
    name = models.CharField(max_length=255, unique=True,primary_key=True)

class Review(models.Model):
    reviewer_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    rating = models.FloatField()
    comment = models.TextField()
    booking = models.ForeignKey('Booking', on_delete=models.CASCADE)
    lawyer_id = models.ForeignKey('Lawyer', on_delete=models.CASCADE)


class Lawyer(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    photo = models.CharField(max_length=255,null=True, blank=True)
    location = models.CharField(max_length=255)
    wilaya = models.CharField(max_length=255)
    lng = models.FloatField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    specialities = models.ManyToManyField('Specialities', blank=True)
    rating = models.FloatField(null=True, blank=True)
    reviews = models.ManyToManyField('Review', blank=True,null=True)
    languages = models.ManyToManyField('Language', blank=True)

class Booking(models.Model):
    lawyer_id = models.ForeignKey('Lawyer', on_delete=models.CASCADE)
    client_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    
