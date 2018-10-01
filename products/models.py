from django.db import models


# Create your models here.
class Product(models.Model):
    #title
    title = models.CharField(max_length=255)
    #image
    image = models.ImageField(upload_to='images/', default=None, blank=True)
    #summary
    readme = models.TextField(default='', blank=True)
    #body
    body = models.FileField(upload_to='templates/', default=None, blank=True)
    #pdf doc file
    doc = models.FileField(upload_to='pdf/',default=None, blank=True)
    #flash_code
    flash_code = models.FileField(upload_to='hex/', default=None, blank=True)
    #fuse
    flash_fuse = models.ImageField(upload_to='images/', default=None, blank=True)
    #CRC
    flash_crc = models.CharField(max_length=10, default='', blank=True)
    #version_flash
    flash_version = models.CharField(max_length=10, default='', blank=True)



    def __str__(self):
        return self.title


    def summary(self):
        return self.readme[:200] + '...'


