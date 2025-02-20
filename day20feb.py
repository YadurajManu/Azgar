
print("First 40 multiples of 7:")
for i in range(1, 41):
    print(i * 7, end=" ")
print("\n")


num = int(input("Enter a 6-digit number: "))
sum_digits = 0
for digit in str(num):
    sum_digits += int(digit)
print("Sum of digits:", sum_digits)


while True:
    user_input = int(input("Enter a number (loop will stop if it's a multiple of 3): "))
    if user_input % 3 == 0:
        break
print("You entered a multiple of 3, exiting loop.")


print("Pattern:")
for i in range(1, 6):
    print("*" * i)

num = int(input("Enter a number to find the product of its digits: "))
product = 1
for digit in str(num):
    product *= int(digit)
print("Product of digits:", product)