from django.shortcuts import render
from .models import Clima
from datetime import date

# Create your views here.

def home(request):
    chuvas = Clima.objects.all()
    clima_hj = Clima.objects.filter(data=date.today())
    data_hj = date.today()
    #data_hj = data_hj.strftime('%d,%m,%Y')

    #quantidade total de chuva para o dia, mes e ano
    chuva_mes_qtd = 0
    chuva_ano_qtd = 0
    for chuva in chuvas:
        if chuva.data == data_hj:
            chuva_hj_qtd = chuva.qtd
        
        if chuva.data.month == data_hj.month and chuva.data.year == data_hj.year:
            chuva_mes_qtd += chuva.qtd

        if chuva.data.year == data_hj.year:
            chuva_ano_qtd += chuva.qtd
        
        if chuva.data.year == chuva.data.year - 1:
            diferenca = chuva_hj_qtd - chuva.qtd
            


    #porcentagem de diferença entre ano anterior
    

    context = {
        'chuva_hj_qtd': chuva_hj_qtd, 
        'chuva_mes_qtd': chuva_mes_qtd,
        'chuva_ano_qtd':chuva_ano_qtd,
        'data_hj': data_hj,
              
    }
    return render(request, 'appHasse/home.html', context )