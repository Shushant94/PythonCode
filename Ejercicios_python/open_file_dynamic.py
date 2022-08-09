#lee el texto y comprueba de que forma esta seperado el paragrafo cuando la maquina sabe de manera que esta lo separado
#entonce nos develue el symbol de la separacion
def process_give_split_symbol(filename):

    file = open(filename)
    #split_symbol = input('Tell me the how do you want to cut word:')
    symbol = [' ',';','-','|','#','~','%','&','{','[',']'
              '}','?','¿','+','-','*']
    dic_machine = dict()
    count = 0
    #first_line = file.readline()

    #for letter in first_line:

    # recorre la linea
    for words in file:
         #recorre por letra
         for letter in words:
           #recorrer la array del symbolo
           for symb in range(len(symbol)):
               #comprueba si el simbolo parece igual que la letra
               if letter == symbol[symb]:
                   #almacena el symbolo como el key y en vaule esta contando cuando symbolos hay
                   dic_machine[symbol[symb]] = dic_machine.get(symbol[symb],0)+1

    file.close()
    #comprueba cual de los symbolo tiene el mayor symbolo
    symbl_key = None
    count_value = None
    for symb,count_symb in dic_machine.items():
        if count_value == None or  count_value < count_symb:
            count_value = count_symb
            symbl_key = symb

    return symbl_key

filename = input('Give me the filename:')
file = open(filename)
array_valor =[]
for line in file:
    print(line)
    word = line.split(process_give_split_symbol(filename))
    array_valor.append(word[0])

