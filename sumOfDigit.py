#n=123 o/p 6
n=int(input("Enter a no. : "))
sum=0
while (n!=0):
    rem=n%10
    sum=sum+rem
    n=n//10
print(sum)