# write a pgm to check if a person is eligible for discount the criteria is he must be studnent and age must be a student and age must be below 21
age=int(input("Enter age :"))
role=input("Enter role: ").lower()
print("Eligible : ",bool(age<21) and role=='student')