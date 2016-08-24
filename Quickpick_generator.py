def order_check(integer,array):
    for z in array:
        if integer<z:
            return True
import random
num_pick = int(input("How many quick picks? "))

for x in range(num_pick):
    lotto_line = []
    lotto_line += [random.randrange(1,40)]
    for i in range(1,5):
        entry= int(random.randrange(1,45))
        order = order_check(entry,lotto_line)
        while (entry in lotto_line) or (order==True) or (entry>40+i):
            entry = random.randrange(1, 45)
            order = order_check(entry, lotto_line)
            #print(entry)
        lotto_line+=[entry]
    print(lotto_line)



