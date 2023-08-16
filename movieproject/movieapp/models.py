from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=250,null=False)
    desc = models.TextField(null=False)
    year = models.IntegerField(null=False)
    img = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name