from django.db import models


class user(models.Model):
    full_name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    

    def __str__(self) -> str:
        return self.full_name

class Message(models.Model):
    time = models.DateTimeField()
    sender =  models.ForeignKey(user,on_delete=models.CASCADE,related_name="+")
    users = models.ManyToManyField(user)
    content = models.TextField()

