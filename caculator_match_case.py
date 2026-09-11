a=float(input("Enter 1st no. : "))
b=float(input("Enter 2nd no. : "))
choice=input("Enter symbols like [+ - * / % // **] :")
match choice:
    case '+':
        print("Addition : ",a+b)
    case '-':
        print("Subtraction : ",a-b)
    case '*':
        print("Multiply : ",a*b)
    case '/':
        if b==0:
            print("Zero is not divide")
        else:
            print("Division : ",a/b)
    case '%':
        print("Remainder : ",a%b)
    case '//':
        if b==0:
            print("Zero is not divide")
        else:
            print("Floor Division : ",a//b)
    case '**':
        print("Power : ",a**b)
    case _:
        print("Invalid Choice")