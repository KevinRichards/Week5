months_num = int(input("How many months? "))
pay_list = []
total = 0
for i in range(months_num):
    pay_list += [input("Enter income for month {}: ".format(i+1))]

print("Income report")
print("------------------")
for x in range(months_num):
    total += float(pay_list[x])
    print("Month {} - Income: $ {:>10,.2f}  Total: $ {:>10.2f}".format((x+1),float(pay_list[x]),total))





