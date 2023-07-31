from django.db import models

# Create your models here.
class journal(models.Model):

    npp = models.IntegerField('№ п/п',null=True,blank=True,max_length=4000)
    dateReg = models.DateField('Дата регистрации приказа',null=True,blank=True)
    content = models.CharField('Краткое содержание',null=True,blank=True,max_length=4000)
    executor = models.CharField('Ответственный за подготовку приказа',null=True,blank=True,max_length=4000)
