num_list = []
sum = 0
for i in range(5):
    num = int(input("Number: "))
    sum+=num
    num_list+=[num]

print("The first number is {}".format(num_list[0]))
print("The last number is {}".format(num_list[4]))
print("The smallest number is {}".format(min(num_list)))
print("The largest number is {}".format(max(num_list)))
print("The average number is {:.2f}".format(sum/5))
