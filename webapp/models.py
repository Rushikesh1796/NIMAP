from django.db import models

# Create your models here.

class clients(models.Model):
    client_id=models.IntegerField()
    client_name=models.CharField(max_length=10)
    created_at=models.DateTimeField()
    created_by=models.CharField(max_length=10)

class projects(models.Model):
    project_id=models.IntegerField()
    project_name=models.CharField(max_length=18)
    created_at=models.DateTimeField()
    created_by=models.CharField(max_length=15)

