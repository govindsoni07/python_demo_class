score = int(input("Enter score: "))

if score >= 1 and score <= 100:
    if score >= 90:
        print("O Grade")
    elif score >= 80:
        print("A Grade")
    elif score >= 65:
        print("B Grade")
    elif score > 35:
        print("C Grade")
    else:
        print("F Grade")
else:
    print("Invalid")
