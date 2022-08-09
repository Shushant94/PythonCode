#Este ejercicio consiste en Añadir una nueva línea del texto dentro un fichero utilizando el array. 
file = open('Read_file.txt','r')
array_line = list()
max_length_line = None
for line in file:
    array_line.append(line.strip())
file.close()


while True:
    try:
        usr_txt = input('Añade texto')
    except:
        print('\n'+'Se ha detenido el programa')
        quit()
    if usr_txt == 'stop':
        break
    else:
      try:
         pos_insert = input('En que línea quieres insertar el código')
      except:
         print('\n'+'Se ha detenido el programa')
         quit()
      #En esta condicion lo que hago es indicar la posición al cuál quiero añadir el texto.  
      if int(pos_insert) < len(array_line):
            array_line.insert(int(pos_insert),usr_txt)
            print('Se ha añadido el texto')

      else:
           array_line.append(usr_txt)

#escribe línea por línea en un fichero txt  recorriendo la  array     
file_w = open('Read_file.txt','w')

for list in array_line:
    file_w.write(list+'\n')
file_w.close()

file_r = open('Read_file.txt','r')
for line in file_r:
    print(line.strip())
