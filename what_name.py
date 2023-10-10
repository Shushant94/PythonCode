#Who likes it?
def likes(names):
    cadena = ""
    if bool(names) == False:
        cadena = "no one likes this"
    elif len(names) == 1:
        cadena = f"{names[0]} likes this"
    elif len(names) == 2:
        cadena = f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        cadena = f"{names[0]}, {names[1]} and {names[2]} like this"
    elif len(names) - 2 >= 2:
        cadena = f"{names[0]}, {names[1]} and {len(names) - 2} others like this"

    return cadena

