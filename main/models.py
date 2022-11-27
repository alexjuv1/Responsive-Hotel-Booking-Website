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
        return ("Room Number: "+str(self.room_number) +" "+ "Price per night: $" + str(self.price_per_night) + "\n" + "Single: "+ str(self.single)+ "\n" + "Smoking: "+ str(self.smoking) + "\n" + "Stars: "+ str(self.stars))

class users(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField(default = 0)
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
    client_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    days_spent = models.IntegerField()
    total_price = models.IntegerField()
    review = models.TextField(default = "NONE")
    def __str__(self):
        return(self.room_id + " " + self.client_id)

class reservation(models.Model):
    room_id = models.ForeignKey(room, on_delete=models.DO_NOTHING)
    client_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    start_date1 = models.IntegerField()
    end_date1 = models.IntegerField()
    def __str__(self):
        return(self.room_id + " " + self.client_id)

class testmod(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="tmod", null=True)
    test1 = models.CharField(max_length=200, default="NONE")
    def __str__(self):
        return(this.name1)
    

