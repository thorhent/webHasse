import sqlite3
"""
from BoaSafra.models import Clima

Clima.objects.create(tempo='Sol', qtd=0, data='2025-1-1')

dias = [i+1 for i in range(28)]
meses = [i+1 for i in range(12)]

aux_dia = 0
aux_mes = 0

for i in range(365):
    while aux_dia < 28:
        
        aux_dia += 1
    
    aux_mes += 1
    aux_dia = 0
    if aux_mes > 11:
        break

"""


with sqlite3.connect(database='db.sqlite3') as conn:
    cursor = conn.cursor()
    
    
    anos = 30
    aux_ano = 2024
    cont = 0
    
    while cont < anos:
        aux_dia = 1
        aux_mes = 1
        for i in range(336):
            while aux_dia <= 28:
                cursor.execute(f"insert into BoaSafra_clima(tempo, qtd, data) values ('Sol', 0, '{aux_ano}-{aux_mes}-{aux_dia}')")
                print(f"cadastrado Sol, 0, {aux_ano}-{aux_mes}-{aux_dia}")
                print(f"cont = {cont}")
                print(f"aux_ano = {aux_ano}")

                conn.commit()
                aux_dia += 1
            
            aux_mes += 1
            aux_dia = 1
            if aux_mes > 12:
                break
            
        
        aux_ano -= 1
        cont += 1
        print(aux_ano)
        print(cont)
    
    
    
    



