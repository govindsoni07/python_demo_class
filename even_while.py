# ch=int(input("Enter range : "))
# i=1
# while i<=ch:
#     i+=1
#     if i%2==0:
#         print(i)


ch=int(input("Enter range : "))
i=1
count=0
odd=0
while i<=ch:
    if i%2==0:
        count+=1
    else:
        odd+=1
    i+=1
print("Even : ",count)
print("Odd : ",odd)