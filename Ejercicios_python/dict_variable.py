#Imprime el valor que hay en la array
Info_person = dict()
datas= ['dni','name','surname','age','sex']

for dat in datas:
    insert_data = input('insert your '+ dat+':')
    Info_person[dat] = insert_data

print(Info_person)
