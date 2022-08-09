#En este ejercico numebro la array de manera aletoria 
import random
Edades = {'Jaun':79, 'Pepito':24,'Yanito':32,'Ernar':38,'Pepe':65}
nombres = list(Edades)

print(nombres[random.randrange(0,len(nombres))])
