import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()

#Busca todos los elemtos llamados counrty y almacenalo en la array
for country in root.findall('country'):
 #Busca me el rank
   rank = country.find('rank').text
 #consigue el elemento
   name = country.get('name')
   print(name,rank)
