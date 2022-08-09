import xml.etree.ElementTree as ET

#EN ESTE EJERCIO SELECIONA EL ELMENTO NEIGHBOR 
tree = ET.parse('country_data.xml')
root = tree.getroot()

for element_select in root.iter('neighbor'):
    print(element_select.attrib)

