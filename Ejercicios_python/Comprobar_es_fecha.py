import re
#En este ejercicio consiste en comprobar si el dia ,més y el año son correctos o no.
months ={'01':31,'02':28,'03':31,'04':30,'05':31,
         '06':30,'07':31,'08':31,'09':30,'10':31,
         '11':30,'12':31}
user = input('Tell me the exactly date 00/00/0000:')
first_slash = user[2:3]
second_slash = user[5:6]


if first_slash == '/' and  second_slash == '/':
 #busca todos los número y lo almacena en una array  
 fecha = re.findall('[0-9]+',user)
 day = fecha[0]
 month = fecha[1]
 year = fecha[2]

if int(month) <= 12 and  int(day) <= months[month]  and len(year) == 4:
    print('fecha es correcta ')

else:
    print("No es una fecha ")
