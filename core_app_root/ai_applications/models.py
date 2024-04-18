from django.db import models

# Create your models here.
class TextModel(models.Model):
    text_body=models.TextField(null=True,blank=True)