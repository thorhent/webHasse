from django.shortcuts import render
from .models import Clima
from datetime import date

# Create your views here.

def home(request):
    climas = Clima.objects.all()
    #clima_hj = Clima.objects.filter(data=date.today())
    data_hj = date.today()
    #data_hj = data_hj.strftime('%d,%m,%Y')
    ano = data_hj.year

    #quantidade total de chuva para o dia, mes e ano
    chuva_mes_qtd = 0
    chuva_ano_qtd = 0
    chuva_hj_qtd = 0
    lista_clima_y1 = [0 for i in range(12)]
    lista_clima_y2 = [0 for i in range(12)]
    lista_clima_y3 = [0 for i in range(12)]
    lista_clima_y4 = [0 for i in range(12)]
    lista_clima_y5 = [0 for i in range(12)]
    
    #variaveis para mes atual
    for clima in climas:
        if clima.data == data_hj:
            chuva_hj_qtd = clima.qtd
        
        if clima.data.month == data_hj.month and clima.data.year == data_hj.year:
            chuva_mes_qtd += clima.qtd

        if  clima.data.year == data_hj.year:
            chuva_ano_qtd += clima.qtd

    #variaveis para ano atual e 2 ultimos anos (grafico)
    #define qtd de chuva por mes
    for clima in climas:
        #ano atual
        if clima.data.year == data_hj.year:
            #somar qtd de chuva por cada mes e armazenar em uma lista ordenada por mes
            lista_clima_y1 = somar_chuvas_mensais(clima, lista_clima_y1)
             
        #ano retrasado
        if clima.data.year == data_hj.year-1:
            lista_clima_y2 = somar_chuvas_mensais(clima, lista_clima_y2)
        
        #3 anos atrás
        if clima.data.year == data_hj.year-2:
            lista_clima_y3 = somar_chuvas_mensais(clima, lista_clima_y3)

        #4 anos atrás
        if clima.data.year == data_hj.year-3:
            lista_clima_y4 = somar_chuvas_mensais(clima, lista_clima_y4)

        #5 anos atrás
        if clima.data.year == data_hj.year-4:
            lista_clima_y5 = somar_chuvas_mensais(clima, lista_clima_y5)


    #definir lista de anos e quantidade de chuva
    lista_anos = definir_qtd_anos(climas)
    
    lista_final = definir_chuva_anos(lista_anos, climas, True)
    
    lista_final = sorted(lista_final, reverse=True)
    
    qtd_anos = len(lista_anos)

    identificador = True
    context = {
        'chuva_hj_qtd': chuva_hj_qtd, 
        'chuva_mes_qtd': chuva_mes_qtd,
        'chuva_ano_qtd':chuva_ano_qtd,
        'data_hj': data_hj,
        'lista_clima_y1': lista_clima_y1,
        'lista_clima_y2': lista_clima_y2,
        'lista_clima_y3': lista_clima_y3,
        'lista_clima_y4': lista_clima_y4,
        'lista_clima_y5': lista_clima_y5,
        'lista_final':lista_final,
        'ano':ano,
        'qtd_anos': qtd_anos,
        'identificador':identificador,      
    }
    return render(request, 'BoaSafra/home.html', context )

def graficos(request, ano, intervalo):
    #climas = dados do ano selecionado
    climas = Clima.objects.filter(data__year=ano)
    #todo banco de dados
    climas_full = Clima.objects.all()
    
    #definido grafico de linhas por dias e grafico de barra por meses
    chuvas = []
    dias = []
    lista_meses_chuva = [0 for i in range(12)]
    for clima in climas:
        dias.append(clima.data.day)
        chuvas.append(clima.qtd)
        lista_meses_chuva = somar_chuvas_mensais(clima, lista_meses_chuva)

    #definir quantos anos estão cadastrados. Retorna uma lista com os anos sem repetição
    anos = definir_qtd_anos(climas_full)
    lista_chuva_anos = definir_chuva_anos(anos, climas_full, False)
    
    intervalo = int(intervalo)
    i = len(lista_chuva_anos)
    while i > intervalo:
        lista_chuva_anos.pop()
        anos.pop()
        i -= 1
    
    #grafico pie chart  ['Nublado', 'Chuva', 'Sol'] | todos
    lista_tempo = definir_tempo(climas_full)
    #grafico pizza | ano
    lista_tempo_ano = definir_tempo(climas)
    for i in range(3):
        if climas_full:
            lista_tempo[i] = round((lista_tempo[i]/len(climas_full))*100)
        if climas:    
            lista_tempo_ano[i] = round((lista_tempo_ano[i]/len(climas))*100)

    identificador = False

    context = {
        'dias': dias,
        'anos':anos,
        'chuvas': chuvas,
        'ano': ano,
        'lista_tempo': lista_tempo,
        'lista_meses_chuva': lista_meses_chuva,
        'lista_chuva_anos': lista_chuva_anos,
        'intervalo': intervalo,
        'lista_tempo_ano': lista_tempo_ano,
        'identificador': identificador,
    }

    return render(request, 'BoaSafra/graficos.html', context)


def somar_chuvas_mensais(clima, lista_clima):
    
    #janeiro == 1, fevereiro == 2
    if clima.data.month == 1:
        lista_clima[0] += clima.qtd
    elif clima.data.month == 2:
        lista_clima[1] += clima.qtd    
    elif clima.data.month == 3:
        lista_clima[2] += clima.qtd    
    elif clima.data.month == 4:
        lista_clima[3] += clima.qtd 
    elif clima.data.month == 5:
        lista_clima[4] += clima.qtd   
    elif clima.data.month == 6:
        lista_clima[5] += clima.qtd
    elif clima.data.month == 7:
        lista_clima[6] += clima.qtd        
    elif clima.data.month == 8:
        lista_clima[7] += clima.qtd    
    elif clima.data.month == 9:
        lista_clima[8] += clima.qtd    
    elif clima.data.month == 10:
        lista_clima[9] += clima.qtd    
    elif clima.data.month == 11:
        lista_clima[10] += clima.qtd
    elif clima.data.month == 12:
        lista_clima[11] += clima.qtd           

    
    return lista_clima


def definir_qtd_anos(climas):
    lista_anos = []
    for clima in climas:
        if clima.data.year not in lista_anos:
            lista_anos.append(clima.data.year)
    
    return lista_anos

def definir_tempo(climas_full):
    lista_tempo = [0,0,0]
    for clima in climas_full:
        if clima.tempo == 'Nublado':
            lista_tempo[0] += 1
        elif clima.tempo == 'Chuva':
            lista_tempo[1] += 1
        else:
            lista_tempo[2] += 1
    
    return lista_tempo

#se chave = True, então método para home, senão para gráficos
def definir_chuva_anos(lista_anos, climas, chave):
    lista_qtd = [0 for i in range(len(lista_anos))]
    lista_final = []
    for i in range(len(lista_anos)):
        for clima in climas:
            if lista_anos[i] == clima.data.year:
                lista_qtd[i] += clima.qtd
            
        lista_final.append([lista_qtd[i], lista_anos[i]])

    if chave:
        return lista_final
    else:
        return lista_qtd
