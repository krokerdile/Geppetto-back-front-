from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    body=models.TextField()
    name=models.CharField(max_length=200)
    age=models.IntegerField(default=0)
    phone=models.CharField(max_length=200)

    def __str__(self):
        return self.title