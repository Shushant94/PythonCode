from datetime import date
import re
class Person():
    Name=""
    Surname=""
    Date_birth=""
    def __init__(self,Name,Surname,Date_birth):
        self.name = Name
        self.Surname= Surname
        self.Date_birth= Date_birth

    def process_check_is_adult(self):
        boolean_value = False
        year_born_per = re.findall('[0-9]{4}',self.Date_birth)

        current_year = date.today().year
        Age_of_person = int(current_year) - int(year_born_per[0])

        if Age_of_person < 18:
            boolean_value = False
        else:
            boolean_value = True

        return boolean_value

class User(Person):
    email=""
    password=""
    def __init__(self,Name,Surname,Datebirth,email,password):
        #Super nos indica la classe lo cúal estamos heredando además utiliza el __init__ del padre
        super().__init__(Name,Surname,Datebirth)

        self.email = email
        self.password = password

    def process_check_account(self):

        boolean_email = False
        boolean_password = False
        boolean_account = False
        email_brand_check = False
        domain_brand_check = False

        # email
        email_brand = ['@hotmail', '@yahoo', '@gmail']
        nombre_domino = ['.com', '.es', '.org']
        # nombre del email ej: shushant
        nombre_email_long = len(self.email[0:self.email.find('@')])
        # nombre de la marca email ej: yahoo,hotmail,gmail
        brand_email_of_user = self.email[self.email.find('@'):self.email.find('.')]
        # nombre del dominio ej: com , org ,es
        user_domino_nom = self.email[self.email.find('.'):len(self.email)]

        # comprueba si en la array tiene yahoo,hotmail,gmail
        if brand_email_of_user in email_brand:
            email_brand_check = True

        # comprueba si en la array tiene com es or org
        if user_domino_nom in nombre_domino:
            domain_brand_check = True


        # comprubea si el la marca del email,el dominio del email conciden o no, ademas comprueba si el nombre del email tiene la longitud mayor que 6
        if email_brand_check == True and domain_brand_check == True and nombre_email_long >= 6 and nombre_email_long <= 30:
            boolean_email = True

        # Ccomprueba si la contraseña tiene estos caracteres
        if re.search('[a-zA-Z0-9$#@]', self.password) and not re.search('\s', self.password) and len(
                self.password) == 6:
            boolean_password = True

        if boolean_email == True and boolean_password == True:
            boolean_account = True

        return boolean_account

        def getEmail(self):
            print(self.email)

        def getPassword(self):
            print(self.password)


#Llamar la class

UserAccount = User("Sam","Chester",'17/06/1993','Samchester19@gmail.com','eT4#0i')
#Comprueba si el usario es adulto
if UserAccount.process_check_is_adult() == True:
        print("EL usuario es adulto")
else:
    print("EL usuario no es adulto")

#Comprueba el email y la contraseña
if UserAccount.process_check_account() == True:
    print("El diseño del email y contraseña es correcta")
else:
    print("EL email o la contrseña no esta correcta")
