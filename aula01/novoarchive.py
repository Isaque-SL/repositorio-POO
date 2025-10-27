from datetime import datetime
from datetime import timedelta

data = "29/10/2025"
horarios = []
h_ini = "09:00"
h_fin = "12:00"
i = 0 # inicio de novos horários
n = int(h_fin.split(":")[0]) - int(h_ini.split(":")[0])
intervalo = 13 # duração de cada horário
c = 0 # quantidade de horários criados

horario_str = f"{data} {h_ini}"
horario = datetime.strptime(horario_str, "%d/%m/%Y %H:%M")
for i in range(n):
    print(horario)
    print("Minutos:", horario.minute, sep="\n")
    horario += timedelta(minutes=intervalo)

# print(horario)
# while i <= n:
#     i += intervalo
#     c += 1
# print(c)