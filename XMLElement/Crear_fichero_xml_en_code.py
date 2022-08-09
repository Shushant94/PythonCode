import xml.etree.ElementTree as ET
#EN ESTE EJERCICIO LO HE HECHO ES CREAR ELEMENTO XML A TRAVES DEL CÓDIGO PYTHON 
datos = {'toni':{'Edad':24,
                 'sexo':'M',
                 'trabajo':'Anticuario'},
         'Ramon':{'Edad':30,
                  'sexo':'M',
                  'trabajo':'Carpintero'},
         'Pepe':{'Edad':25,
                 'sexo':'M',
                 'trabajo':'Ingeniero'

         },
         'Antonia':{'Edad':40,
                    'sexo':'F',
                    'trabajo':'Diseñadora'

         }
        }
        
#ELEMENTO RAIZ        
elm_tree = ET.Element('datos_personales')
#RECORRE EL DICCIONARIO Y MUESTRA CLAVE Y VALOR 
for nombre,datas in datos.items():
    #elemento data sobre
    data_of_each_person = ET.SubElement(elm_tree,'data_sobre')
    #atributo del datos personales
    #EJEMPLO <data_sobre nombre='Shushant'></data_sobre>
    data_of_each_person.set('nombre',nombre)
#RECORRER OTRO DICCIONARIO DENTRO DE VALOR Y MUESTRAME OTRO LLAVE Y VALOR   
    for info_elm,info_data in datas.items():
#EJEMPLO <data_sobre nombre='Shushant'>
	    	#<Edad>
	    	    #24
	    	#</Edad>
    	#</data_sobre>
        info_element = ET.SubElement(data_of_each_person,info_elm)
        info_element.text = str(info_data)
#GUARDAME TODOS LOS ELEMENTOS CREADO EN UNA RAIZ   
tree = ET.ElementTree(elm_tree)
#ESCRIBEMELO EN UN FICHERO XML EL ELEMENTO CREADO  
tree.write('Información_personal.xml',encoding='UTF-8')
