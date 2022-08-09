import xml.etree.ElementTree as ET

#abre el fichero
tree = ET.parse('Arboles.xml')
#obten todo el elemento
root = tree.getroot()

for elm_father in root:
    #Si dentro de child tag hay más elemento o no
    if elm_father:
        for child in elm_father:
            print(child.text)


