import re
def arithmetic_arranger(array_artich,perform_the_operation):

    array_first_number=list()
    array_second_number=list()
    array_operation = list()
    Verification_boolean=list()
    Error_print =""
    result=""

    #CHECK HOW MUCH ARITHMETIC NUMBER WE HAVE
    if len(array_artich) <=5:
        #CHECK THE SYMBOL
        for Numbers in array_artich:
            for digit in Numbers.strip():
                if digit == '+' or digit == '-':
                    Verification_boolean.append(True)
                    array_operation.append(digit)

        #VALIDATE THE SYMBOL
        if Verification_boolean.count(True) != len(array_artich):
            Error_print = "Error operation must be + or -"
        else:
            Verification_boolean.clear()

            for position in range(0,len(array_artich)):
                #SEPARATE THE NUMBER
                Number = array_artich[position]
                num =Number[0:Number.find(array_operation[position])].strip()
                second_num=Number[Number.find(array_operation[position])+1:len(Number)].strip()

                #CHECK IS NUMBER OR NOT
                if num.isdigit() and second_num.isdigit():
                    Verification_boolean.append(True)
                    array_first_number.append(int(num))
                    array_second_number.append(int(second_num))
            #CHECK IF EACH NUMBER IS DIGIT OR NOT
            if Verification_boolean.count(True) != len(array_artich):
                Error_print = "Error number only contain digits"

            #ARITHMETIC DESIGN
            else:

                dash = "-------"
                first_number = ""
                symbol_with_second_number = ""
                line = ""

                value_of_caculation=""
                for i in range(0, len(array_first_number)):
                    first_number = first_number + str(array_first_number[i]).rjust(10)

                first_number = "\n" + first_number

                for j in range(0, len(array_first_number)):
                    symbol_with_second_number = symbol_with_second_number + array_operation[j].rjust(6) + str(array_second_number[j]).rjust(
                        4)


                symbol_with_second_number = "\n" + symbol_with_second_number

                for k in array_first_number:
                    line = dash.rjust(10) + line

                line = "\n"+ line

            for pos in range(0, len(array_first_number)):
                if array_operation[pos] == "+":
                    calculate = int(array_first_number[pos]) + int(array_second_number[pos])
                    value_of_caculation = value_of_caculation + str(calculate).rjust(10)
                elif array_operation[pos] == "-":
                    calculate = int(array_first_number[pos]) - int(array_second_number[pos])
                    value_of_caculation = value_of_caculation + str(calculate).rjust(10)

            value_of_caculation ="\n"+value_of_caculation


            #IF VALUE ES TRUE SHOW THE RESULT ELSE ONLY SHOW THE ARITHMETIC
            if perform_the_operation == True:
                result = first_number  + symbol_with_second_number + line  + value_of_caculation
            elif perform_the_operation == False:
                result = first_number + symbol_with_second_number + line
    else:
        Error_print = "Error: Too many problems"

    if Error_print != "":
        return Error_print
    else:
        return result

print(arithmetic_arranger(['254 + 157','345 - 658','784 + 789','111 - 879','111 + 879'],True))


