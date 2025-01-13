from django.db import models

# Create your models here.
from django.db import models


# Create your models here.

class Clima(models.Model):
    """
        Modelo para definir quantidade de chuva (mm) em um dia específico de 
        um lugar específico.
    """
    TIPO_TEMPO = (
        (u'Sol',u'Sol'),
        (u'Nublado',u'Nublado'),
        (u'Chuva',u'Chuva'),
    )
    
    tempo = models.CharField("Tempo do dia", choices=TIPO_TEMPO, max_length=50)
    qtd = models.IntegerField("quantidade de chuva (mm)", default=0, help_text='Quantidade de milímetros (mm) de chuva. Exemplo: 25')
    data = models.DateField("data de chuva", editable=True, unique=True)
    

    class Meta:
        verbose_name = 'Clima'
        verbose_name_plural = 'Climas'

    
    def __str__(self):
        return self.tempo + ' para o dia ' + str(self.data) 

    def __unicode__(self):
        return self.tempo + 'para o dia' + str(self.data) 

    