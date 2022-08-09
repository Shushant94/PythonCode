import random
import colorama
from colorama import Fore

#Este ejercico se basa en saber el resultado de suma, resta, división o multiplicación 

#Try y catch: si el valor que haya insertado no es integer entonces haz un excepción y muestra me el error 
try:
   
    print("This game is about to do the operation")
    number_selected = input('Select the number:')
    select_operation = input('Select the operation:')
    select_the_range_number = input('Select the range number')
    point = 10;
except:
    print("The user don't put any vaule ")
    #Detiene el código 
    quit()

time = 10
#Si la puntuación el mayor que 1 entonces sigue este bulce 
while point > 1:
      #guardamen el rango de número aleatoria que haya indicado en una variable llamada random_number 
      random_number = random.randrange(0,int(select_the_range_number))
      
      #Si número seleccionado es mayor que numero aleatorio entra aqui y imprime la tres variables en un orden concreto si no imprime de otra forma 
      #ejemeplo 2+3=? o 4+2=?  
      #ejemplo numero selccionado : 3 numero aleatorio: 2
      if int(number_selected) > random_number:
        
        print(number_selected,select_operation,random_number,'=?')
      else:
          print(random_number, select_operation, number_selected, '=?')
     
     
      #Si el usuario en vez de integer escribe cadena entonces deten el código y muestrame el error 
      try:
        answer = input('answer:')
      except:
          print("The user don't put any answer")
          quit()
      #si la cadena es stop deten el código  
      if answer == 'stop':
          break
      else:
      #Comprueba si la operación es suma además verifica el resultado del usario   
          if select_operation == '+':
            result = int(number_selected) + random_number

            if str(result) == str(answer):
              point = point +1
              print(Fore.GREEN +'corret', 'point:',point)
            else:
                point = point -1
                print(Fore.RED + 'incorret the answer is :',result, 'point:', point)
        #Comprueba si la operación es resta 
          elif select_operation == '-':

              if int(number_selected) > random_number:
                  result = int(number_selected) - random_number
                  print(result)
                  if str(result) == str(answer):
                      point = point + 1
                      print(Fore.GREEN + 'corret', 'point:', point)
                  elif result != answer:
                      point = point - 1
                      print(Fore.RED + 'incorret the answer is :',result, 'point:', point)


              else:

                result =  random_number - int(number_selected)
                print(result,answer)
                if str(result) == str(answer):
                    point = point + 1
                    print(Fore.GREEN +'corret', 'point:', point)
                else:
                    point = point - 1
                    print(Fore.RED +'incorret the answer is :',result,point)
	#Comprueba si es multipicación  
          elif select_operation == '*':
              result = int(number_selected) * random_number
              if str(result) == str(answer):
                  point = point + 1
                  print(Fore.GREEN +'corret', 'point:', point)
              else:
                  point = point - 1
                  print(Fore.RED +'incorret the answer is :',result, 'point:', point)
	#COmprueba si el división 
          elif select_operation == '/':

             if random_number != 0:

                  print(random_number)
                  if int(number_selected) > random_number:

                    result = int(number_selected) / random_number

                    if str(result) == str(answer):
                        point = point + 1
                        print(Fore.GREEN + 'corret', 'point:', point)
                    else:
                        point = point - 1
                        print(Fore.RED +'incorret the answer is :', result, 'point:', point)



                  elif int(number_selected) < random_number:
                    result = random_number / int(number_selected)

                    if type(result) == int:
                        if str(result) == str(answer):
                                point = point + 1
                                print(Fore.GREEN +'corret', 'point:', point)
                        else:
                                point = point - 1
                                print(Fore.RED +'incorret the answer is :', result, 'point:', point)
                    else:
                        if str(result) == str(answer):
                            point = point + 1
                            print(Fore.GREEN +'corret', 'point:', point)
                        else:
                            point = point - 1
                            print(Fore.RED + 'incorret the answer is :', result, 'point:', point)

print('game over')
print('point',point)

