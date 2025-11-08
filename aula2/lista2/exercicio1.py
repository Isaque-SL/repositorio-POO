from datetime import datetime, timedelta

tempo = timedelta(hours=10, minutes=30)

data = datetime(2010, 11, 30)
new_data = data + tempo
print(tempo)
print(data + tempo)
print(new_data)