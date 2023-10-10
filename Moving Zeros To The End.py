array = [1, 0, 1, 0, 0, 1, 3]
count_zero = array.count(0)
not_zero = list(filter(lambda x: x > 0, array))
for n in range(0,count_zero):
   
    not_zero.append(0)
print(not_zero)