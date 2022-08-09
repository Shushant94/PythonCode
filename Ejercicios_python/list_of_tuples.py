#COMPRUEBO LA FUNCIONALIDAD DEL TUPLE 
list_tup = {'a':10,'b':5,'c':30 }

list_acedent = sorted(list_tup.items())
tmp = list()
dic_tmp = dict()
for k,v in list_acedent:
    print(k,v)

for k,v in list_tup.items():
    tmp.append((v,k))
    dic_tmp[k] = v

tmp = sorted(tmp,reverse=True)
#ORDENAME EL CLAVE Y EL VALOR Y QUE SEA AL REVÉS 
print(sorted([(k,v) for k,v in list_tup.items()],reverse=True))
#ORDENAME LA LLAVE Y EL VALOR 
print(sorted([(v,k) for k,v in list_tup.items()]))
#ORDENAME EL LLAVE Y VALOR 
print(sorted([k for k,v in dic_tmp.items()]))

tuple = list_tup
list = []
print(tuple.items())

