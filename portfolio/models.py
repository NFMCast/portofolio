from django.db import models
from datetime import datetime

# Create your models here.

class BlogPost(models.Model):
    autor = models.CharField(max_length=50)
    data = models.DateField(default=datetime.today().strftime('%Y-%m-%d'))
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo
