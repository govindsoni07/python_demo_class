#wap to to calculate the of using match case with function
def calculator(a,b,operation):
    match operation:
        case '+':
            print("addtion : ",a+b)
        case '-':
            print("subtraction : ",a+b)
        case '*':
            print("Multiply : ",a*b)
        case '/':
            print("Division : ",a/b)
        case '%':
            print("Remainder : ",a%b)
        case _:
            print("Invalid operation")

a=int(input("Enter 1st no. "))
b=int(input("Enter 2nd no. "))
op=input("Enter operation : ")
calculator(a,b,op)