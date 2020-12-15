option = None
while option != "6":
    print("1) Multiplication")
    print("2) Division")
    print("3) Addition")
    print("4) Subtraction")
    print("5) Prime Number")
    option = input("> ")
    if option == "1":
        numberOne = float(input("Input first number: "))
        numberTwo = float(input("Input second number: "))
        solution = numberOne * numberTwo
        print(str(numberOne) + " * " + str(numberTwo) + " = " + str(solution))

    elif option == "2":
        numberOne = float(input("Input first number: "))
        numberTwo = float(input("Input second number: "))
        solution = numberOne / numberTwo
        print(str(numberOne) + " / " + str(numberTwo) + " = " + str(solution))

    elif option == "3":
        numberOne = float(input("Input first number: "))
        numberTwo = float(input("Input second number: "))
        solution = numberOne + numberTwo
        print(str(numberOne) + " + " + str(numberTwo) + " = " + str(solution))

    elif option == "4":
        numberOne = float(input("Input first number: "))
        numberTwo = float(input("Input second number: "))
        solution = numberOne - numberTwo
        print(str(numberOne) + " - " + str(numberTwo) + " = " + str(solution))

    elif option == "5":
        number = input("Enter max number: ")
        print("Number is: " + number)
        print("The prime numbers are as follows: ")
        for x in range(1, int(number) + 1):
            if x != 2 and x % 2 == 0:
                continue
            elif x != 3 and x % 3 == 0:
                continue
            elif x != 5 and x % 5 == 0:
                continue
            elif x != 7 and x % 7 == 0:
                continue
            elif x != 11 and x % 11 == 0:
                continue

            print(x)

    print()