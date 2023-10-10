import re
def pig_it(text):
    modify = ""
    write="ay"
    words = text.split()
    for word in words:
        if re.match("[^\w\s]",word.strip()):
            modify = modify+word
        else:
            modify = modify+word[1:]+word[0]+write.ljust(3)
    return modify.strip()