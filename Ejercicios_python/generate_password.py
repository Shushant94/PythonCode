import random
#EN ESTE EJERCIO LO QUE HE HECHO ES CREAR UNA CONTRASEÑA COMPLICADA 
insert_quanty_crater = input('Longitud de la cadena que deseas:')
abecedario =['a','b','c','d','e','f','g','h','i','j',
               'k','l','m','n','o','p','q','r','s','t',
               'u','v','w','x','y','z']
upper_abecedario = list()

for upper_leter in abecedario:
    upper_abecedario.append(upper_leter.upper())
numero = ['0','1','2','3','4','5','6','7','8','9']
simbolo =['/','|','@','~','{','[',']','}','~','!','"',
         '·','$','%','&','/','(',')','=','?','¿','^',
         '*','¨','_','-','*']
#Aqui lo que he hecho es almacenar los tres array para así poder seleccionar de forma aleatoria 
char = [abecedario,upper_abecedario,simbolo,numero]
password =''

for i in range(int(insert_quanty_crater)):
     #dentro de esta array selecciona el indice aleatoriamente
     #ejemplo char[upper_abecedario] 
     list_inside = char[random.randrange(0,4)]
     
     #dentro del list_inside selecciona el indicie aleatoriamente
     #ejemplo list_inside['A'] 
     password = password + list_inside[random.randrange(0,len(list_inside))]

    #password = password+char[random.randrange(0,3)]
print(password)
