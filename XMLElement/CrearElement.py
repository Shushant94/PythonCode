import xml.etree.ElementTree as ET

#elemento raiz
element_raiz = ET.Element('a')
#subelemetos
element_b = ET.SubElement(element_raiz,'b')
#subelemento
element_c = ET.SubElement(element_b,'c')
#subelemento
element_d = ET.SubElement(element_c,'d')
ET.dump(element_raiz)
