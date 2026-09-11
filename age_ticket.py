#if age is less than 12 the 10 % discount given otherwise not
age=int(input("Enter age : "))
ticket=int(input("Enter ticket value : "))
if age<12:
    print("Wow ---- 10% Off\nFinal Price is :",ticket-(ticket*10/100))
else:
    print("No Disoucnt\nFinal Price is : ",ticket)