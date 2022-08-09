import requests
import json
#En este ejercicio concsite que en una página tiene información en formato json y lo que tiene que hacer coger esos datos almacenar en un array   
data = requests.get('https://api.covid19api.com/summary').json()
newdeadths_data = list()
id = list()
for dat in data["Countries"]:
     for key,value in dat.items():
        if key == 'NewDeaths':
          newdeadths_data.append([key,value])
        elif key == "ID":
            id.append([key,value])

for newdead in newdeadths_data:
    print(newdead)
for idtify in id:
    print(idtify)


