from datetime import datetime

data = "29/10/2025"
horarios = []
h_ini = "09:00"
h_fin = "12:00"
i = 0 # inicio de novos horários
n = h_fin - h_ini
intervalo = 13 # duração de cada horário
c = 0 # quantidade de horários criados

horario = datetime()
while i <= n:
    i += intervalo
    c += 1
print(c)