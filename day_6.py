
age = int(input("Enter your age: "))

if age <= 12:
    print("Life Stage: Child")
elif 13 <= age <= 19:
    print("Life Stage: Teenager")
elif 20 <= age <= 35:
    print("Life Stage: Young Adult")
elif 36 <= age <= 60:
    print("Life Stage: Adult")
else:
    print("Life Stage: Senior Citizen")


num = int(input("Enter a number to check divisibility: "))

if num % 5 == 0 or num % 7 == 0:
    print("The number is divisible by 5 or 7.")
else:
    print("The number is not divisible by 5 or 7.")


percentage = float(input("Enter your percentage: "))

if 90 <= percentage <= 100:
    print("Grade: A")
elif 80 <= percentage < 90:
    print("Grade: B")
elif 70 <= percentage < 80:
    print("Grade: C")
elif 60 <= percentage < 70:
    print("Grade: D")
else:
    print("Grade: Fail")
    