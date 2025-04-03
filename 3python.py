
"""L = [11, 12, 14, 15, 23, 25, 28, 30, 32, 34]
i = 0
while i < len(L):
    if L[i] % 2 == 0:
        L.pop(i)
    else:
        i += 1  
print(L)



students = {
    "Arushi": 85,
    "Vanya": 78,
    "Yadu": 92,
    "Rahul": 74,
    "Manu": 88
}
print("Student Marks Dictionary:", students)"""

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

concatenated_tuple = tuple1 + tuple2
print("Concatenated Tuple:", concatenated_tuple)

repeated_tuple = tuple1 * 3
print("Repeated Tuple:", repeated_tuple)



numbers_tuple = (11, 25, 36, 48, 52, 67, 72, 89, 90, 100)

max_value = max(numbers_tuple)
min_value = min(numbers_tuple)
sum_values = sum(numbers_tuple)

print("Tuple:", numbers_tuple)
print("Maximum:", max_value)
print("Minimum:", min_value)
print("Sum:", sum_values)



num = int(input("Enter a 3-digit number: "))

if 100 <= num <= 999:
    sum_of_digits = sum(int(digit) ** 3 for digit in str(num))
    if num == sum_of_digits:
        print(num, "is an Armstrong number.")
    else:
        print(num, "is not an Armstrong number.")
else:
    print("Please enter a valid 3-digit number.")
