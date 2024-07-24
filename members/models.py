from django.db import models
# Create your models here.



class Members(models.Model):
    id = models.BigAutoField(primary_key=True,editable=False)
    email = models.CharField(max_length=100, null=True)
    password =  models.CharField(max_length= 100, null=True)
    
