from django.db import models

# Create your models here.
class Disposal(models.Model):
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    address=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    writer=models.CharField(max_length=200)
    item=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    etc=models.TextField()
    photo = models.ImageField(upload_to="image/")

    def __str__(self):
        return self.title