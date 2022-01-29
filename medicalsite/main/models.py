from django.db import models
from django.contrib.auth.models import User

class Medical_entries(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    email = models.EmailField(max_length=254)
    posted_on = models.DateField()
    med_id=models.AutoField(auto_created = True,primary_key=True)