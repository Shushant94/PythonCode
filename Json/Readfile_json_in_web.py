#EN ESTE EJERCICIO LEEO EL DESDE LA PÁGINA WEB LOS DATOS DEL JSON Y LO ALMACENO EN UNA ARRAY 
import requests
import json
response = requests.get('https://api.covid19api.com/summary').text
print(response)
js = json.loads(response)
total_conf = []
for country in js['Countries']:
    #alamacena en la array otros dos array en la posicón 0 y en la posición 1
    total_conf.append([country['Country'],country['TotalConfirmed']])


for total in total_conf:
    print(total)



#https://towardsdatascience.com/json-and-apis-with-python-fba329ef6ef0
