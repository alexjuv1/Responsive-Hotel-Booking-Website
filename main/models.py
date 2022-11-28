from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class room(models.Model):
    reserved = models.BooleanField()
    room_number = models.IntegerField()
    price_per_night = models.IntegerField()
    single = models.BooleanField()
    smoking = models.BooleanField()
    stars = models.IntegerField()

    def __str__(self):
        return ("Room Number: "+str(self.room_number) +" "+ "Price per night: $" + str(self.price_per_night) + "\n" + "Single: "+ str(self.single)+ "\n" + "Smoking: "+ str(self.smoking) + "\n" + "Stars: "+ str(self.stars))

class users(models.Model):
    # email = models.CharField(max_length=255, blank=True)
    # password = models.CharField(max_length=255, blank=True)
    #id = models.IntegerField(primary_key = True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=255)
    # age = models.IntegerField(default = 0, blank=True)
    # status = models.CharField(max_length=255, blank=True)
    #django_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    #django_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    def __str__(self):
        return (self.first_name + " " + self.last_name)

class admin(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length = 255)
    def __str__(self):
        return (self.email)

class history(models.Model):
    room_id = models.ForeignKey(room, on_delete=models.DO_NOTHING)
    client_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    days_spent = models.IntegerField()
    total_price = models.IntegerField()
    review = models.TextField(default = "NONE")
    def __str__(self):
        return(self.room_id + " " + self.client_id)

class reservation(models.Model):
    room_id = models.ForeignKey(room, on_delete=models.DO_NOTHING)
    client_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    start_date1 = models.DateField()
    end_date1 = models.DateField()
    def __str__(self):
        return(self.room_id + " " + self.client_id)

class testmod(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="tmod", null=True)
    test1 = models.CharField(max_length=200, default="NONE")
    def __str__(self):
        return(this.name1)
    

