import json
#EN ESTE EJERCICIO LO QUE HE HECHO ES CREAR UN DICCIONARIO Y CARGAR DE FORMATO JSON
data ='''{
    "name": "chuck",
    "phone": {
      "type" :"intl",
      "number": "+1 734 303 4456"
    },
    "email" : {
      "hide":"yes"
    }
}'''
info = json.loads(data)
print('Name:',info["name"])
print('Hide:',info["email"]["hide"])

for key,value in info.items():
    print(value)
