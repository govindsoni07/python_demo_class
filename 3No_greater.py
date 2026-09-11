a=int(input("Enter 1st no. "))
b=int(input("Enter 2nd no. "))
c=int(input("Enter 3rd no. "))

if a>b and a>c:
    print(f"{a} is greater")
elif b>a and b>c:
    print(f"{b} is greater")
else:
    print(f"{c} is greater")
