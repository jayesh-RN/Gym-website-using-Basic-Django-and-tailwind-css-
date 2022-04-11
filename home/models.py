from django.db import models

# Create your models here.

# makemigration - create changes and store in a file
# migrate - apply the pending changes created by makemigrations

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    phone =  models.CharField(max_length=12)
    date = models.DateField()
    
    def __str__(self):
        return self.name