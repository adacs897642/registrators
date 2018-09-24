from django.db import models

# Create your models here.
class Products(models.Model):
    #title
    title = models.CharField(max_length=255)
    #image
    image = models.ImageField(upload_to='images/')
    #body
    body = models.TextField()

    def __str__(self):
        return self.title
