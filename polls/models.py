from django.db import models
from django.contrib.auth.models import User

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    name = models.CharField(max_length=200) 
    description = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)  
    frequency = models.CharField(
        max_length=50,
        choices=[
            ('daily', 'Daily'),
            ('weekly', 'Weekly'),
            ('monthly', 'Monthly')
        ],
        default='daily'
    ) 

    def __str__(self):
        return self.name
    
class Progress(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    date = models.DateField() 
    status = models.BooleanField()  

    def __str__(self):
        return f"{self.habit.name} - {self.date}: {'Completed' if self.status else 'Missed'}"
