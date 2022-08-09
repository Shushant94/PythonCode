
#En este ejercicio consiste en hacer una pareja de 2 en dos o en tres en tres si sobra una pues mostralo separado  

#this code is made by shushant
nombres = ['Samnta', 'Ana','Tania','Rina','Leila','Miriam','Tamara','Lopez','Antonia']
boolean_value = True
user_select = input('Selecciona cantidad de nombre que quieras seleccionar:')

#si el valor es true sigue el bucle
while boolean_value:
    #valor sobrado
    surplus_value = len(nombres)
#si indice de la array es 0 para el bucle
    if surplus_value == 0:
        break
#si sobran dos o 1 valor dentro de la array entra aquí
    elif surplus_value == 1 or surplus_value == 2:
        print(nombres[0:1])
        nombres.pop(0)
#si el valor no es 0,1 o 2 entra aquí
    else:
#si el programa peta muestrame este error
      try:
	#Selecciona el indice desde 0 hasta el numero que haya indicado         
        print(nombres[0:int(user_select)])
        
        print(len(nombres))
        #elimina la array 
        for i in range(int(user_select)):
          nombres.pop(0)
      except:
          print("El numero que haz introducido no es valido")
          quit()

