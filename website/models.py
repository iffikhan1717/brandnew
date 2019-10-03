from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=66)
    img = models.ImageField(upload_to='bimages/')
    desc = models.TextField()



    def __str__(self):
        return str(self.title)

