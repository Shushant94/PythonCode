import re
class AddUser:
    Name=''
    Surname=''
    date_of_birth=''
    email=''
    password = ''

    #init es una instancia creada por pyhon que se le puede llamar el contuctor
    def __init__ (self,Name,Surname,date_of_birth,email,password):
        self.Name = Name
        self.Surname = Surname
        self.date_of_birth = date_of_birth
        self.email = email
        self.password = password

#Comprueba si el email que ha introducido es correcto o no  
    def process_check_data(self):
        fecha_str = re.findall('[0-9]+', self.date_of_birth)
        day = fecha_str[0]
        month = fecha_str[1]
        year = fecha_str[2]
        months = {'01': 31, '02': 28, '03': 31, '04': 30, '05': 31,
                  '06': 30, '07': 31, '08': 31, '09': 30, '10': 31,
                  '11': 30, '12': 31}
        email_brand_check = False
        domain_brand_check = False
        # email
        email_brand = ['@hotmail', '@yahoo', '@gmail']
        nombre_domino = ['.com', '.es', '.org']
        #nombre del email ej: shushant
        nombre_email_long = len(self.email[0:self.email.find('@')])
        #nombre de la marca email ej: yahoo,hotmail,gmail
        brand_email_of_user = self.email[self.email.find('@'):self.email.find('.')]
        #nombre del dominio ej: com , org ,es
        user_domino_nom = self.email[self.email.find('.'):len(self.email)]

        #comprueba si en la array esta este yahoo,hotmail,gmail
        if brand_email_of_user in email_brand:
            email_brand_check = True
        else:
            email_brand_check == False

        #comprueba si en la array esta el dominio com es or org
        if user_domino_nom in nombre_domino:
            domain_brand_check = True
        else:
            domain_brand_check = False


        boolean_check = dict()
       #Comprobar si el valor es un nombre si lo es muestra me True
        if not self.Name.isdigit() and not self.Name.isdigit():
            boolean_check['nombre'] = True
            boolean_check['apellido'] = True
        else:
            boolean_check['nombre'] = False
            boolean_check['apellido'] = False
        #Comprueba si es fecha y que dia y més tenga dos digitos y el año se de 4 digitos
        if self.date_of_birth[2:3] == '/' and self.date_of_birth[5:6] == '/' and int(month) <= 12 and int(day) <= months[month] and len(
                year) == 4:
            boolean_check['fecha'] = True

        else:
            boolean_check['fecha'] = False

        #comprubea si el la marca del email,el dominio del email conciden o no, ademas comprueba si el nombre del email tiene la longitud mayor que 6
        if email_brand_check == True and domain_brand_check == True and nombre_email_long >= 6 and nombre_email_long <=30:
            boolean_check['email'] = True
        else:
            boolean_check['email'] = False
        #Ccomprueba si la contraseña tiene estos caracteres
        if re.search('[a-zA-Z0-9$#@]',self.password) and not re.search('\s',self.password) and len(self.password) == 6:
            boolean_check['password'] = True
        else:
            boolean_check['password'] = False


        return boolean_check

    def getName(self):
        print(self.Name)
    def getSurname(self):
        print(self.Surname)
    def getdate_of_birth(self):
        print(self.date_of_birth)
    def getEmail(self):
        print(self.email)
    def getPassword(self):
        print(self.password)
