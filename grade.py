score=int(input("Enter score : "))
if score>=90 and score<=100:
    print("O Grade")
elif score>=80 and score<=90:
    print("A Grade")
elif score>=65 and score<=80:
    print("B Grade")
elif score>35 and score<=65:
    print("C Grade")
elif score<=35:
    print("F Grade")
else:
    print("Invalid")