from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class room(models.Model):
    reserved = models.BooleanField()
    room_number = models.IntegerField()
    price_per_night = models.IntegerField()
    single = models.BooleanField()
    smoking = models.BooleanField()
    stars = models.IntegerField()

    def __str__(self):
        return (str(self.room_number))

class users(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    status = models.CharField(max_length=255)
    def __str__(self):
        return (self.first_name + " " + self.last_name)

class admin(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length = 255)
    def __str__(self):
        return (self.email)

class history(models.Model):
    room_id = models.ForeignKey(room, on_delete=models.DO_NOTHING)
    client_id = models.ForeignKey(users, on_delete=models.DO_NOTHING)
    days_spent = models.IntegerField()
    total_price = models.IntegerField()
    review = models.TextField()
    def __str__(self):
        return(self.room_id + " " + self.client_id)

class reservation(models.Model):
    room_id = models.ForeignKey(room, on_delete=models.DO_NOTHING)
    client_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    start_date1 = models.IntegerField()
    end_date1 = models.IntegerField()
    def __str__(self):
        return(self.room_id + " " + self.client_id)


