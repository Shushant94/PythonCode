import xml.etree.ElementTree as ET
# EN ESTE EJERCICIO LO HACEMOS ES MODIFICAR EL ARCHIVO XML  
tree = ET.parse('country_data.xml')
root = tree.getroot()
#iter() lo que hace es selccionar solo ese elemento indicado  
for rank in root.iter('rank'):
    #SUMA UN NÚEMRO 
    write_rank = int(rank.text) +1
    #TRANSFORMA EN UN STRING Y ESCRIBE EN EL ELMENTO RANK 
    rank.text = str(write_rank)
    rank.set('update','yes')
#ESCRIBE EN EL ELEMENTO RAIZ 
tree.write('output.xml')

