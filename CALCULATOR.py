def main():
    print("WELCOME TO BASIC CALCULATOR")
    print("1.ADDITION")
    print("2.Subtraction")
    print("3.Multiply")
    print("4.Division")
    PO = input("Pick? ")
    if float(PO) > float(4):
        print('ERROR')
    if float(PO) > float(4):
        quit(0)
    num1 = input("Number 1 ")
    num2 = input("Number 2 ")
    'printing the sum'
    if PO == '1':
        print("=", float(num1) + float(num2))
    elif PO == '2':
        print("=", float(num1) - float(num2))
    elif PO == '3':
        print("=", float(num1) * float(num2))
    elif PO == '4':
        print("=", float(num1) / float(num2))
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "yes":
        main()
    else:
        quit()
main()