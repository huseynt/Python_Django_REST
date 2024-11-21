from django.db import models



# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    age = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    json = models.JSONField()
    

    def __str__(self):
        return self.name