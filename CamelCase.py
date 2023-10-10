import re
Camel_case = "the_steal_warrior"
#Divide el texto cunado encuentres estos dos simbolos "-_" y almacena en la array
words = re.split("[_-]",Camel_case)
first_pos = ""

word=""
print(Camel_case.count("_"))
#Si hay dos símbolos entra en esta condición
if Camel_case.count("_") >= 2:
    #coje la array de la posicion 0 y selecciona la primera letra y cambias en minuscula y guntas resto del la palabra
    first_pos = words[0][0].lower()+words[0][1:]
    #recorre el bulce de la palabras
    for Capital_letter in range(1,len(words)):
        #en cada palabra o articulo pones en mayuscula
        first_pos = first_pos + words[Capital_letter][0].upper()+words[Capital_letter][1:]

else:
    for Capital_letter in words:
            #selecciona la palabra y en la primera posicion pones en mayuscula
            first_pos = first_pos + Capital_letter[0].upper()+Capital_letter[1:]
print(first_pos)
