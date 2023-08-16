from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=250,null=False)
    img = models.ImageField(upload_to='pics',null=False)
    contact = models.CharField(max_length=10,null=False)
    email = models.EmailField(max_length=50,null=False)

    def __str__(self):
        return self.name