from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Entry(models.Model):
    class Meta:
        ordering = ['-created_at', '-id']
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, 
                               on_delete=models.CASCADE, 
                               related_name="entries")
    
    def __str__(self):
        return f"Заметка {self.author.username} {self.created_at.strftime("%d.%m.%Y %H:%M")}"