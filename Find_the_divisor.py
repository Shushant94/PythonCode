def divisor(integer):
    can_divide_with = list()
    operator= 0
    prime = ""
    for i in range(1,integer):
            if integer%i == 0 and i > 1:
                print(i)
                can_divide_with.append(i)
            elif integer//i == integer and integer//integer == 1 :
                prime = f"{integer} is prime"

    if len(can_divide_with) >= 1:
        return can_divide_with
    elif len(can_divide_with) == 0:
        return prime

print(divisor(29))

def divd(num):
    l = [i for i in range(2,num) if num%i == 0]
    if len(l) == 0:
        return str(num) + "is prime"
    return l
print(divd(29))
