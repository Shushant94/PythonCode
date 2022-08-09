#EN ESTE EJERCICIO LO QUE HEHCO ES UN COMPROBACIÓN BÁSICA DE ELEMETO ROOT(RAIZ),TAGS Y SUS ATTRIBUTOS  
#ElementTree representa toda el elemeto xml
#Element representa solo un nodo del arbol
import xml.etree.ElementTree as ET

#data = '''<person>
#         <name>chuck</name>
#        <phone type="intl">
#            +1734 303 44556
#       </phone>
#        <email hide="yes"/>
#        </person>'''
#tree =ET.fromstring(data)
#print('Name:',tree.find('name').text)
#print('atrr:',tree.find('email').get('hide'))

#Selecciona el archivo
tree = ET.parse('country_data.xml')
#obtener todo el elemento
root = tree.getroot()
#Es el elemento raiz
print(root.tag)
#El elemento raiz no tiene atributo
print(root.attrib)

#muestra la ruta donde esta dicho archivo
#muestrame los hijo del dicho raiz
for child in root:
    for tag_year in child:
        if tag_year.attrib:
            print(tag_year.attrib)

        if tag_year.tag == 'year':
            print(tag_year.text)
