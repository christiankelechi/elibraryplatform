from django.db import models

# Create your models here.
class Books(models.Model):
    book_title=models.CharField(max_length=2000)
    
