from django.db import models

# Create your models here.
class User(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=100)
    
    
    # name = models.CharField(max_length=100)
    # email = models.CharField(max_length=100)
    # password = models.CharField(max_length=100)
    # phone = models.CharField(max_length=100)
    # address = models.CharField(max_length=100)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name