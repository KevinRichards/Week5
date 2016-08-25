def sorter(array):
    i = 0
    while i<5:
        a = array[i]
        b = array[i+1]
        if a>b:
            array[i] = b
            array[i+1] = a
            i = 0
        else:
            i +=1
    return array
def main():
    import random
    num_pick = int(input("How many quick picks? "))

    for x in range(num_pick):
        lotto_line = []
        print('   ')
        for i in range(0,6):
            entry= int(random.randrange(1,41+i))
            while (entry in lotto_line):
                entry = int(random.randrange(1, 41 + i))
            lotto_line+=[entry]
        sorter(lotto_line)
        for x in range(0,6):
            print('{:2}'.format(lotto_line[x]), end=" ")
main()