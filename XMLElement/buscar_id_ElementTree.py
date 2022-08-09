import xml.etree.ElementTree as ET
#EN ESTE EJERCICIO LO QUE ESTOY HACIENDO ES MOSTRAR EL ARTTRIBUTO HIJO  
#ESCOJE LA RUTA DEL ARCHVIO 
tree = ET.parse('documentos.xml')
#ESCOJE EL ELEMENTO PADRE 
root = tree.getroot()

#RECCORRE EL ELEMENTO PADRE 
for elm_father in root:
    if elm_father:
#RECORRE EL ELEMENTO HIJO 
        for elm_child in elm_father:
#ESCOJE SI EL ELEMENTO HIJO TIENE ID         
            if elm_child.attrib.get('id'):
                print(elm_child.attrib)

