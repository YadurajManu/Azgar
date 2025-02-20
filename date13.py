# 1. Print all multiples of 13 from 187 to 555 and their sum
total_sum = 0
for i in range(187, 556):
    if i % 13 == 0:
        print(i, end=" ")
        total_sum += i
print("\nTotal Sum:", total_sum)

# 2. Print 'n' multiples of 11 and their sum
n = int(input("Enter value of n: "))
total_sum = 0
for i in range(1, n+1):
    print(11 * i, end=" ")
    total_sum += 11 * i
print("\nTotal Sum:", total_sum)

# 3. Reverse a 6-digit number and check if it is a palindrome
num = int(input("Enter a 6-digit number: "))
rev_num = int(str(num)[::-1])
print("Reversed Number:", rev_num)
if num == rev_num:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")

# 4. Print the given series: 2, 5, 8, 11, 14, 17, 20... up to n terms
n = int(input("Enter number of terms: "))
a, d = 2, 3
for i in range(n):
    print(a, end=" ")
    a += d
print()

# 5. Apply the given operations until the number becomes 1 and count steps
num = int(input("Enter a positive number: "))
steps = 0
while num != 1:
    print(num, end=" ")
    if num % 2 == 0:
        num //= 2
    else:
        num = num * 3 + 1
    steps += 1
print("1")
print("Total steps taken:", steps)
