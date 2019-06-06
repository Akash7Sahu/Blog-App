from django.db import models


# Create your models here.
class Blog(models.Model):
    name=models.CharField(max_length=30)
    body=models.TextField()
    pic=models.FileField(upload_to='images/')
    upload_date=models.DateTimeField(auto_now_add=True)
    author=models.CharField(max_length=30)
    def __str__(self):
        return self.name
