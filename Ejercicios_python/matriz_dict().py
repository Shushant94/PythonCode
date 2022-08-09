
#EN ESTE EJERCICO COMPRUEBO LA FUNCIONALIDAD DEL DICCIONARIO Y EL METODO ITEM()
horarios ={'Lunes':{'8:00 a 10:00':'Programación',
                    '10:00 a 11:00':'Taxi',
                    '11:00 a 12:00':'Castellano',
                    '12:00 a 13:00':'Mates'},
          'Martes':{'8:00 a 10:00': 'tarea de casa',
                     '10:00 a 11:00': 'pedir_cita',
                     '11:00 a 12:00': 'Castellano',
                     '12:00 a 13:00': 'Mates'},
          'Miercoles':{'8:00 a 10:00':'Programación',
                        '10:00 a 11:00':'Taxi',
                        '11:00 a 12:00':'Castellano',
                        '12:00 a 13:00':'Mates'},
          'Jueves':{'8:00 a 10:00':'Programación',
                    '10:00 a 11:00':'Taxi',
                    '11:00 a 12:00':'Castellano',
                    '12:00 a 13:00':'Mates'}
        }

for semanas,horas in horarios.items():
    print(semanas)
    for hora,assignatura in horas.items():
        print(hora,':',assignatura)
