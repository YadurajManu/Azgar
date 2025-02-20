# Q1

str1 = "Hello"
str2 = "World"
str3 = "Python"

print("H" in str1)  
print("z" not in str2)  
print("Py" in str3)  

#Q2
num1 = int(input("Enter first three-digit number: "))
num2 = int(input("Enter second three-digit number: "))
num3 = int(input("Enter third three-digit number: "))
num4 = int(input("Enter fourth three-digit number: "))

a = num1
a += num2
print("Addition assignment (+=):", a)

b = num3
b -= num4
print("Subtraction assignment (-=):", b)

c = num1
c *= num2
print("Multiplication assignment (*=):", c)

d = num3
d //= num4
print("Floor division assignment (//=):", d)

e = num1
e %= num2
print("Modulus assignment (%=):", e)

#Q3
x = True
y = False

print("Logical AND:", x and y)  
print("Logical OR:", x or y)  
print("Logical NOT:", not x) 

a = 5  
b = 3  

print("Bitwise AND:", a & b)  
print("Bitwise OR:", a | b)  
print("Bitwise XOR:", a ^ b)  

#Q4
import math

r = float(input("Enter radius of the cone: "))
h = float(input("Enter height of the cone: "))

l = math.sqrt(r**2 + h**2)  
curved_surface_area = math.pi * r * l
volume = (1/3) * math.pi * r**2 * h

print("Curved Surface Area:", curved_surface_area)
print("Volume of Cone:", volume)




