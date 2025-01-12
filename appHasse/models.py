from django.db import models
from datetime import date

# Create your models here.

class Clima(models.Model):
    """
        Modelo para definir quantidade de chuva (mm) em um dia específico de 
        um lugar específico.
    """
    qtd = models.IntegerField("quantidade de chuva (mm)", help_text='Quantidade de milímetros (mm) de chuva. Exemplo: 25')
    data = models.DateField("data de chuva", editable=True, unique=True)

    class Meta:
        verbose_name = 'Clima'
        verbose_name_plural = 'Climas'

    def __str__(self):
        return 'da data '+str(self.data) 

    def __unicode__(self):
        return 'da data '+str(self.data) 