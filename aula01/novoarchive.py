from datetime import datetime
from datetime import timedelta

data = "29/10/2025"
horarios = []
h_ini = "23:00"
h_fin = "01:00"
intervalo = 30 
horario_ini_str = f"{data} {h_ini}"
horario_fin_str = f"{data} {h_fin}"
horario_final = datetime.strptime(horario_fin_str, "%d/%m/%Y %H:%M")
horario = datetime.strptime(horario_ini_str, "%d/%m/%Y %H:%M")
horarios.append(horario)
if horario_final < horario:
    horario_final += timedelta(days=1)

while horario < horario_final:
    horario += timedelta(minutes=intervalo)
    horarios.append(horario)

for i in horarios:
    print(i)
