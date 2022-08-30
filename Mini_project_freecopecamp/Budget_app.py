import math


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()
        self.total_amount = 0

    def deposit(self, amount, description=""):

        self.ledger.append({"amount": amount, "description": description})

    # Save the amount in dict with decription and return True value
    def withdraw(self, amount, description=""):
        took_place = False
        amount = float(amount)
        if self.check_found(amount) == True:
            self.ledger.append({"amount": -amount, "description": description})
            took_place = True
        return took_place

    # Calculate the total amount spended
    def get_balance(self):
        operation = 0
        result = 0
        for pos in range(0, len(self.ledger)):
            if pos != 0:
                operation = self.ledger[pos]['amount'] + operation

        return self.ledger[0]['amount'] - abs(float(operation))

    # save the class and transfer to the withdraw and deposit
    def transfer(self, amount, category):
        took_place = False

        if self.check_found(amount) == True:
            self.withdraw(amount, "Transfer to" + category.name)
            category.deposit(amount, "Transfer to" + self.name)
            took_place = True
        return took_place

    # Check if the amount is lower then deposit
    def check_found(self, amount):
        tookplace = False

        if abs(amount) <= self.ledger[0]['amount']:
            tookplace = True
        return tookplace

    # Print the ticket
    def __str__(self):
        resultado = self.name.center(30, '*') + '\n'
        for pos in range(0, len(self.ledger)):
            list_of_bill = self.ledger[pos]
            price = "{0:.2f}".format(list_of_bill['amount'])
            descrip = list_of_bill['description']

            total_digit_used = len(descrip) + len(str(price))

            rest_space = 30 - total_digit_used + 5
            if pos == 0:
                resultado = resultado + descrip + str(price).rjust(rest_space + 1) + '\n'
            else:
                resultado = resultado + descrip + str(price).rjust(rest_space) + '\n'

        resultado = resultado + "Total:" + str(self.get_balance())
        return resultado

    # Calculate the percentage
    def withdrwals(self):
        total_ticket = 0
        result = 0
        char_number = ""
        for list in range(0, len(self.ledger)):
            if list != 0:
                total_ticket = abs(self.ledger[list]["amount"]) + total_ticket
        # self.total_amount=abs(amount)+self.total_amount
        total_ticket = total_ticket * 100 / 100
        result = math.floor(total_ticket / 10) * 10
        return result


def create_spend_chart(categories):
    catg_perctg = []
    result = ""
    empty_space = ""
    dash = ""
    length_ticket_name = 0
    # Save the each percentage in array
    for catg in categories:
        catg_perctg.append(catg.withdrwals())

    result = result + "Percentage Spent by category" + "\n"

    # Graphic design
    # run 100 to -10 when you reach percentage 0 stop the loop
    for num_percentage in range(100, -1, -10):

        length = len(str(num_percentage))
        # if the lenght of percentage is higher then 2 the give more space
        if length > 2:
            result = result + str(num_percentage) + "|".rjust(3)
        elif length == 1:
            result = result + str(num_percentage) + "|".rjust(5)
        else:
            result = result + str(num_percentage) + "|".rjust(4)

        for list in range(0, len(categories)):
            # check if the postion of percentage is in the same grafic then add the letter o
            if catg_perctg[list] == num_percentage:
                result = result + "o".rjust(2)
                catg_perctg[list] = catg_perctg[list] - 10
            # Else add a space
            else:
                result = result + " ".rjust(1)
        # next line
        result = result + "\n"

    result = result + "\n"

    # Save the higher length letter
    for pos in range(0, len(categories)):
        dash = dash + "-".rjust(2)
        if length_ticket_name < len(categories[pos].name):
            length_ticket_name = len(categories[pos].name)

    result = result + dash.rjust(12) + "\n"
    # print as a matriz the letter
    for i in range(0, length_ticket_name):

        for list in range(0, len(categories)):
            # if the list is 0 give a space on the right side
            if list == 0:
                result = result + " ".rjust(6)
            # if ticket name length is lower then i(length_ticket_name) select one letter of the position we selected
            if i <= len(categories[list].name):

                result = result + categories[list].name[i:i + 1].rjust(2)

            else:
                result = result + empty_space.rjust(2)
        # next line
        result = result + "\n"

    return result




food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
print(food)
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)
print(auto)

print(create_spend_chart([food, clothing, auto]))



