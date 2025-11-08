import datetime
import pytz

# 1. Objeto datetime ingênuo (naive)
data_string = "2023-10-27 10:00:00"
formato = "%Y-%m-%d %H:%M:%S"
dt_naive = datetime.datetime.strptime(data_string, formato)
print(f"Objeto ingênuo: {dt_naive}")

# 2. Definir o fuso horário desejado
fuso_horario = pytz.timezone('America/Sao_Paulo')

# 3. Localizar o objeto datetime com o fuso horário
dt_aware = fuso_horario.localize(dt_naive)
print(f"Objeto cônscio: {dt_aware}")

# Exemplo de conversão para UTC
dt_utc = dt_aware.astimezone(pytz.utc)
print(f"Convertido para UTC: {dt_utc}")
