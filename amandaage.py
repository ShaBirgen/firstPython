# my first python

name = input("Enter name: ")

a = int(input("Enter current year: "))

b = int(input("Enter year of birth: "))


age = a - b

print(name + " is  ")

if age >= 18 and age < 25:
    print("a student ")
elif age >= 14 and age < 18:
    print("a high school child")
elif age < 14:
    print("primary school kid")
else:
    print("old enough to work")
