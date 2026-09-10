a = int(input("Enter no. to check whether the no. is prime or not: "))
prime = 0
for i in range(1, a + 1):
    if a % i == 0:
        prime += 1

if prime == 2:
    print("prime")
else:
    print("not prime")
