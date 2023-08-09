from django.db import models
class Post(models.Model):
  body_text = models.TextField('Texto Principal')
  pub_date = models.DateTimeField('Data Publicação', auto_now=True)

# Create your models here.
