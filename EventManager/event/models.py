from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Work(models.Model):
    EventType=models.CharField(max_length=100)
    Picture=models.ImageField(upload_to='works/')
    Description=models.CharField(max_length=400)

    def __str__(self):
        return self.EventType


class Team(models.Model):
    Name=models.CharField(max_length=100)
    Picture=models.ImageField(upload_to='team/')
    Description=models.CharField(max_length=400)

    def __str__(self):
        return self.Name


class Client(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    Phno=models.CharField(max_length=20)
    Email=models.CharField(max_length=40)

    def __str__(self):
        return self.Name

class Rate(models.Model):
    event_type = models.ForeignKey(Work, on_delete=models.CASCADE)
    price=models.CharField(max_length=700)

    def __str__(self):
        return f"{self.price} - {self.event_type.EventType}"




class BookEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_type = models.ForeignKey(Work, on_delete=models.CASCADE)
    price = models.CharField(max_length=700)
    booking_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('event_type', 'booking_date')

    def __str__(self):
        return f"{self.user.username} - {self.event_type.EventType} on {self.booking_date} for {self.price}"