from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employees(models.Model):
    
    Position = (
        ('manager', 'Manager'),
        ('developer', 'Developer'),
        ('team-leader', 'Team-Leader')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=15, choices=Position)
    salary = models.FloatField(null=True, default=0.0)
    join_date =  models.DateTimeField(null=True)
    
    
    def __str__(self) -> str:
        return self.name