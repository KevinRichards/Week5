def main():
    months_num = int(input("How many months? "))
    pay_list = []
    total = 0
    print("Income report")
    print("------------------")
    for i in range(months_num):
        pay_list += [input("Enter income for month {}: ".format(i+1))]
        total += float(pay_list[i])
        print("Month {} - Income: $ {:>10,.2f}  Total: $ {:>10.2f}".format((i + 1), float(pay_list[i]), total))
main()




