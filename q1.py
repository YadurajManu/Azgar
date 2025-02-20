# 1. Calculate total cost of a shopping cart with 8% sales tax
shirt_price = 2500.99
pants_price = 1500.50
shoes_price = 4500.75
total_cost = shirt_price + pants_price + shoes_price
total_cost_with_tax = total_cost * 1.08
print(f"Total cost including 8% sales tax: Rs. {total_cost_with_tax:.2f}")

# 2. Convert temperature between Fahrenheit and Celsius
fahrenheit = 98.6
celsius = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

celsius = 37
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

# 3. Calculate average speed of a car and convert to miles/h
distance_km = 150  
time_hours = 2     
avg_speed_kmh = distance_km / time_hours
avg_speed_mph = avg_speed_kmh * 0.621371
print(f"Average speed: {avg_speed_kmh:.2f} km/h or {avg_speed_mph:.2f} miles/h")

# 4. Calculate compound interest
P = 10000  
r = 5 / 100  
n = 12  
t = 5  
A = P * (1 + r / n) ** (n * t)
print(f"Compound Interest after {t} years: Rs. {A:.2f}")