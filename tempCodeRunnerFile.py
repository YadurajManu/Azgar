num = int(input("Enter a positive integer: "))
if num < 2:
    print(f"{num} is not a prime number.")
else:
    is_prime = True  
    i = 2  
    while i * i <= num:
        if num % i == 0:
            is_prime = False
            break
        i += 1  
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
