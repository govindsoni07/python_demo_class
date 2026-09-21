n=int(input("Enter a no. : "))  # 123
rem=0
rev=0
while(n!=0):   #123 #12 #1
    rem=n%10    #3  2 1
    rev=(rev*10)+rem  #3 32 321
    n=n//10 #12 1 0
print(rev)
