# regual take input n no. while user not press 'quit' and positive and negaitve no. show
while True:
    n = input("Enter a no. : ")
    if n == 'quit':
        break
    n = int(n)
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")

