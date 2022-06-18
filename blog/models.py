from django.db import models

# Create your models here.
class Post (models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    Created_date = models.DateTimeField(auto_now_add=True)
    Published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
