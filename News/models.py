from django.db import models
# Create your models here.

class New(models.Model):
  title = models.CharField(max_length=150)
  img1 = models.CharField(max_length=50)
  img2 = models.CharField(max_length=50)
  P1 = models.TextField(max_length=400)
  P2 = models.TextField(max_length=400)
  P3 = models.TextField(max_length=400)
  P4 = models.TextField(max_length=400)
  P5 = models.TextField(max_length=400)
  P6 = models.TextField(max_length=400)
  
  def __str__(self):
    return self.title 

class Comment(models.Model):
  Comentario = models.TextField(max_length=250)
  news = models.ForeignKey(New, default="", on_delete=models.CASCADE, related_name='cmm')
  def __str__(self):
    return self.Comentario
