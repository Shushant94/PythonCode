#En este ejericico se basa en contar cuantos letras repetidas hay 
file = open('read_file_python')
counts_word = dict()
texto = list()

for line in file:
	#Split corta en espacio en blanco y lo almacena en una array 
    words = line.split()
    for word in words:
        counts_word[word] =counts_word.get(word,0)+1


bgcount = None
bgname = None

#bucle clave y valor 
#el valor items() muestra los dos datos del diccionario
for word,count in counts_word.items():
    if bgcount == None or count > bgcount:
        bgcount = count
        bgname = word

print('La palabra que se repite es','"',bgname,'"','se repite ',bgcount,'veces')


for word in counts_word.keys():
    print(word)
