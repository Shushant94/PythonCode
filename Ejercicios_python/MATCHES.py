#Expressiones regulares
#son secuencia de carateres que forman patrón de búsqueda
#que es una expressiones regulares
import re
texto = '''Hola Mundo.
Me gusta Python !!!!
Mi primer numero de la suerte es 987-654-321
Mi segundo numero de la suerte es 879-543-210
Mi tercero numero de la suerte es 765-432-100
Mi cuarto numero de la suerte es 123-456-123-123
'''

#Metacarateres
#\d - Digito (0-9)
#r anula otro exprexiones de python
numero='26525415'
print(re.match(r'\d',numero))
#busca todos los emparejamiento
print(re.findall(r'\d',texto))

#busca lo dijito
#print(re.search(r'\d',texto))

#\D - No digitos (0-9)
#\w - Carater (a-z,A-Z,0-9,_)


#^ este simbolo se utiliza comprobar la primera línea de cadena
cadena = "anas"
#busca la primera letra que empieza por a 
if re.findall('^a',cadena):
    print("Empieza por a")
else:
    print('no empieza por a')
    
#busca la última letra que empieza por s 
if re.findall('s$',cadena):
    print('ultima línea es s')
else:
     print('no es s')

file = open('Read_line')

for line in file:

#    if re.match('^F-\S+:', line):
   if re.match('^A\S',line):
     print(line)
     #Comprueba el email 
     if re.match('[a-zA-Z]+@+[a-zA-Z]+(\.[com|es])',line):
        print("email correct")


text = 'my 2 favorite numbers are 19 and 42'
#busca el los numeros y almacenalo en una array 
get_number = re.findall('[0-9]+',text)
print(get_number)
#busca la primera letra con cualquiere caracter más con más valor hasta el  dos puntos   almacenalo en una array 
text_dos = "From: Using the: character:"
get_cadena = re.findall('^F.+:',text_dos)
print(get_cadena)
#busca la primera letra con cualquier caracter que no más caracter 
firt_cadena = "From: Using the: character:"
get_first_cadena=re.findall('^F.+?:',firt_cadena)
print(get_first_cadena)

#busca la 
email = 'From shushant94@yahoo.com Sat Jan 5 09:14:16 2008'
find_email = re.findall('^From (\S+@+\S+)',email)
print(find_email)
password = 'sder'

#busca el arroba y busca si no tiene espacio blanco uno más y almacenalo en
get_email = re.findall('@([^ ]*)',email)

print(get_email)

x = 'We just received 27/06/1994 for cookeies.'
y = re.findall('[0-9]+',x)
print(y)

if re.match('([A-Za-z ]{4,})',password):
    print('password es propiado')
else:
    print('password invalido')
string_n = '02'
print(int(string_n))


