from django.db import models

class Method(models.Model):
    title = models.CharField(max_length=50,verbose_name='Заголовок метода')
    print = models.CharField(max_length=25,verbose_name='Название метода')
    description = models.TextField(verbose_name='Описание метода')
    example_code_image = models.ImageField(upload_to='methods_image/',verbose_name='Изображение примера кода', null=True,blank=True)




class Task(models.Model):
   title = models.CharField(' Название', max_length=50)
   task = models.TextField('Описание')

   def __str__(self):
        return self.title
