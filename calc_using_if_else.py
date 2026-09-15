while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiply")
    print("4. Division")
    print("5. Remainder")
    print("6. Floor Division")
    print("7. Power")
    print("8. Factorial")
    print("0. Exit")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        a = int(input("Enter 1st no. : "))
        b = int(input("Enter 2nd no. : "))
        print("Addition : ", a + b)

    elif choice == 2:
        a = int(input("Enter 1st no. : "))
        b = int(input("Enter 2nd no. : "))
        print("Subtraction : ", a - b)

    elif choice == 3:
        a = int(input("Enter 1st no. : "))
        b = int(input("Enter 2nd no. : "))
        print("Multiply : ", a * b)

    elif choice == 4:
        a = int(input("Enter 1st no. : "))
        b = int(input("Enter 2nd no. : "))
        if b == 0:
            print("Cannot divide by zero")
        else:
            print("Division : ", a / b)

    elif choice == 5:
        a = int(input("Enter 1st no. : "))
        b = int(input("Enter 2nd no. : "))
        print("Remainder : ", a % b)

    elif choice == 6:
        a = int(input("Enter 1st no. : "))
        b = int(input("Enter 2nd no. : "))
        if b == 0:
            print("Cannot divide by zero")
        else:
            print("Floor Division : ", a // b)

    elif choice == 7:
        a = int(input("Enter 1st no. : "))
        b = int(input("Enter 2nd no. : "))
        print("Power : ", a ** b)

    elif choice==8:
        a = int(input("Enter no. : "))
        fac=1
        for i in range(1,a+1):
            fac=fac*i
        print(fac)
    elif choice==0:
        break
    else:
        print("Invalid Choice")
