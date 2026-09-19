n=int(input("Enter a no. "))
count=0
if n==0:
    print("1")
else:
    while(n>0):
        count+=1
        n//=10
print(count)