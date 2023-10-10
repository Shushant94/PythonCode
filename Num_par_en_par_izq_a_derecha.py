cadena="254"
residuo=len(cadena)%2
array=list()
exit=False
if residuo == 1:
  array.append(cadena[0])
  cadena= cadena.replace(cadena[0],'').strip()
while exit == False:
  if len(cadena)==0:
    exit =True
  else:
    array.append(cadena[:2])
    cadena= cadena.replace(cadena[:2],'').strip()
print(array)