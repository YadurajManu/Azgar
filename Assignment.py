
basic_salary = float(input("Enter basic salary: "))

hra = 0.10 * basic_salary
ma = 0.05 * basic_salary
ta = 0.03 * basic_salary

tax = 0.12 * basic_salary
pf = 0.05 * basic_salary

total_allowances = hra + ma + ta
total_deductions = tax + pf

final_salary = basic_salary + total_allowances - total_deductions

if final_salary > 5000:
    bonus = 200
else:
    bonus = 0

print("Final Salary:", final_salary)
print("Bonus:", bonus)
