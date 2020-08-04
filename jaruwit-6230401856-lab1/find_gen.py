import datetime
name = input("Please enter your first name :")
born_age = input("Enter the year you were born :")
born_age = int(born_age)
now = datetime.datetime.now()
current_year = now.year
age = current_year - born_age
gen = " "
if age >= 1 and age <= 9:
    gen = "Alpha"
elif age >= 10 and age <= 24:
    gen = "Z"
elif age >= 25 and age <= 39:
    gen = "Y"
elif age >= 40 and age <= 54:
    gen = "X"
elif age >= 55 and age <= 72:
    gen = "Baby Boomer"
elif age > 72:
    gen = "Builder"
elif age <= 0:
    print("Invalid")
print("", name, "is", age, "year old. You are genaration", gen)
