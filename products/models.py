from django.db import models


# Create your models here.
class Product(models.Model):
    #title
    title = models.CharField(max_length=255, verbose_name='Название')
    #image
    image = models.ImageField(upload_to='images/', verbose_name='Фото', default=None, blank=True)
    #summary
    readme = models.TextField(default='', verbose_name='Краткое описание', blank=True)
    #body
    body = models.FileField(upload_to='templates/', verbose_name='Шаблон страницы описания', default=None, blank=True)
    #fuse
    flash_fuse = models.ImageField(upload_to='images/',verbose_name='Изображение бит программирования', default=None, blank=True)
    #CRC
    flash_crc = models.CharField(max_length=10, verbose_name='CRC прошивки', default='', blank=True)
    #version_flash
    flash_version = models.CharField(max_length=10, verbose_name='Версия прошивки', default='', blank=True)

    class Meta:
        verbose_name = 'Изделие'
        verbose_name_plural = 'Изделие'
        ordering=['title']


    def __str__(self):
        return self.title


    def summary(self):
        return self.readme[:200] + '...'


class ProductDoc(models.Model):
    # hunter
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # title
    title = models.CharField(max_length=255, verbose_name='Название')
    # doc file
    doc = models.FileField(upload_to='file/', verbose_name='Файл')


    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документ'
        ordering=['title']

    def __str__(self):
        return self.title

