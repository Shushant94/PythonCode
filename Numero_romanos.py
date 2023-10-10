output_text = 'LXX'
#Cambiar en mayúscula
numero_romano = output_text.upper()
#suma de numeros total
digit_suma = 0
#numero romanos
signos_romanos={'I':1,'II':2,'III':3,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
#cociente
cociente  = len(numero_romano)//2
#residuo
residuo = len(numero_romano)%2
#suma de cociente y residuo nos da un numero impar
recorrido = cociente + residuo
#guardamos los signos del texto en una array
Signos = list()
#invertimos el texto XXI en IXX para asi poder dividir mejor
revers_cadena = numero_romano[::-1]
#almacenamos la cadena invertida
cadena = revers_cadena

for num in range(0,recorrido):
    #si las letra que hemos eliminado queda 0 entras en esta condición
    if len(cadena) == 0:
        #cuando solo quede una letra romana  añdimos en la array
        Signos.append(cadena[0])
        #borramos en la cadena la letra que hemos guardaos antes para así poder seleccionar sigientes 2 letras
        cadena = cadena.replace(cadena[:2],'')
        #eliminamos el espacio en blanco
        cadena.strip()
    # cuando haya dos letras romana almacena en esta array
    Signos.append(cadena[:2])
    #borramos la letra que esta en la cadena ya que ya hemos almacenado en la array
    cadena = cadena.replace(cadena[:2],'')
    cadena.strip()

#letra separadas en la array
print(Signos)
#lo que hemos alamacenado en la array lo recorremos
for signo in Signos:
    #si hay una letra entonce entra en esta condición
    if len(signo) == 1:
      #suma con los restos de números
      digit_suma = signos_romanos.get(signo) + digit_suma
    else:
        #en signo hay dos letras lo que he hecho compara dos letra si la letra A > B entra en esta condicion y resta lo.
        #por ejemplo CX la letra romana C(100) es mayor que la letra romana X(10) entonces entrará en esta condición y hara la operación
        if signos_romanos.get(signo[0]) > signos_romanos.get(signo[1]):
            digit_suma = signos_romanos.get(signo[0]) - signos_romanos.get(signo[1])+digit_suma
        #si la letra romana es menor entonces entra en esta condición y realiza la suma
        elif signos_romanos.get(signo[0]) < signos_romanos.get(signo[1]):
            digit_suma = signos_romanos.get(signo[0]) + signos_romanos.get(signo[1]) +digit_suma
        # si la dos letra són iguales entra en esta condición y también realiza la suma.
        elif signos_romanos.get(signo[0]) == signos_romanos.get(signo[0]):
            digit_suma = signos_romanos.get(signo[0])+ signos_romanos.get(signo[1]) +digit_suma
print(digit_suma)

