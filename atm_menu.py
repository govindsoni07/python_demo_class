#ATM Machine
# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Exit

balance=0
while True:
    ch=int(input("1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit\n"))
    if ch==1:
        print("Balance : ",balance)
    elif ch==2:
        amt=int(input("Enter amt to deposit : "))
        balance+=amt
        print("---------------Deposit Successfully------------------------")
    elif ch==3:
        if balance<=0:
            print("Insufficent Fund")
        else:
            amt=int(input("Enter amt to withdraw : "))
            if balance>=amt:
                 balance-=amt
                 print("------------Withdraw Successfully---------------------")
            else:
                print("-----------Insufficent withdrawal---------------------")
    elif ch==4:
        break
    else:
        print("Invalid Choice")