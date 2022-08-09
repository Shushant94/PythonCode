#ESTE CÓDIGO QUE HE ESCRITO TIENE LA FUNCIONALIDAD DE COMPROBAR CADA ELEMENTO DE UNA MANERA QUE YO LO INDIQUE A TRAVES DE UN METODO LLAMADO findall()
import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()

#Ecuentra el elemento raiz
top_level_element = root.findall(".")
print(top_level_element)
for raiz in  top_level_element:
    print (raiz.tag)

#busca la ruta que he indicado
top_level_elm_child = root.findall('./country/neighbor')

for top_level in top_level_elm_child:
    print(top_level)

#.//year select all the element
#/.. selecciona la anterior ruta
# [@name= sigapore] selecciona el atributo singapore
#buscame el atributo que tenga singapore y el hijo sea year
get_element_with_attribut = root.findall(".//year/..[@name='Singapore']")
for country in get_element_with_attribut:
    print(country)
# * selecciona todo los granchildren
#selcciona todos los elemento y todos los elementos padres y que atributo se sinfapore y muestra me el año
granchilder = root.findall(".//*[@name='Singapore']/year")
print(granchilder)

#muestrame el segundo neighbor del cada elemento
second_child = root.findall('.//neighbor[2]')
for neighbor in second_child:
    print(neighbor.attrib)

select_spc_tag = root.findall('{*}')
print(select_spc_tag)

#que no sea este atributo indicado
not_this_attrb = root.findall(".//country[@name!='Singapore']")
for attrib in not_this_attrb:
    print(attrib.attrib)

#selecciona todo el emento en el que tag se year
only_tag = root.findall('.//*[year]')
for year in only_tag:
    print(year)
#Selecciona todos los elementos grandchildren y busca todos los atrributo que contengan el value sigapore. 
all_element = root.findall(".//*[.='Singapore']")
for elem in all_element:

  print(elem.attrib)
