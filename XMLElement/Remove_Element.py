import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()

for country in root.iter('country'):
      rank = country.find('rank').text
      if int(rank) > 50:
          #Element
          elemento = country.find('rank')
          #selecciona  elemento especifico y elimina dicho elemento
          country.remove(elemento)
tree.write('country_data.xml')
