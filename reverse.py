n=int(input("Enter a no. : ")) #123
rev=0
while (n!=0):
    rem=n%10 #3   #2 #1
    rev=rem+(rev*10)# 3+0=3 # 32 
    n=n//10 #12  #1 
print(rev)

