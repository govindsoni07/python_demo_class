'''
*
**
***
****
*****
'''
print ("---------------------------Sidha------------------------")

for i in range(1,6):
    for j in range(i):
        print('*',end=" ")
    print()

print ("---------------------------Ulta------------------------")
'''
*****
****
***
**
*
'''
for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

print ("--------------------------Sidha Number print------------------------")
for i in range(1,6):
    for j in range(i):
        print(j+1,end=" ")
    print()
print ("--------------------------Ulta Number print------------------------")
for i in range(5,0,-1):
    for j in range(i):
        print(j+1,end=" ")
    print()
