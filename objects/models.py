from django.db import models

# Create your models here.
class Lpu(models.Model):
    #name
    name = models.CharField(max_length=255, verbose_name='Название эксплуатирующей организации')
    #phone
    phone = models.CharField(max_length=255, verbose_name='Телефон УОИ')
    #img
    img = models.ImageField(upload_to='images/', verbose_name='Фото', default=None,null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ЛПУ'
        verbose_name_plural = 'ЛПУ'
        ordering=['name']

class Object(models.Model):
    #obj_lpu_id

    lpu = models.ForeignKey(Lpu, on_delete=models.CASCADE)
    #name
    name  = models.TextField(verbose_name='Название объекта')
    #phone
    phone = models.CharField(max_length=255, verbose_name='Телефон объекта')
    #project
    project = models.CharField(max_length=255, verbose_name='Номер проекта')

    def __str__(self):
        return self.name[0:100]



    class Meta:
        verbose_name = 'Переход'
        verbose_name_plural = 'Переходы'
        ordering=['name']


class Error(models.Model):
    #id
    obj = models.ForeignKey(Object, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Название')
    error = models.TextField(verbose_name='Описание проблемы')
    time = models.DateTimeField(auto_now=True, verbose_name='Время записи')

    def __str__(self):
        return (self.name[0:100] + ': ' + self.error[0:100])[0:100]

    def pub_date_pretty(self):
        return self.time.strftime('%b %e %Y')

    class Meta:
        verbose_name = 'Проблема'
        verbose_name_plural = 'Проблемы'
        ordering=['name']


class Documents(models.Model):
    obj = models.ForeignKey(Object, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Название')
    file = models.FileField(upload_to='file/', verbose_name='Файл')

    def __str__(self):
        return self.name[0:100]

    class Meta:
        verbose_name = 'Документы перехода'
        verbose_name_plural = 'Документы перехода'
        ordering=['name']

