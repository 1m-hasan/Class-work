def is_prime(n: int) -> bool:

    if (n == 0 or n == 1): return False
    for i in range(2, n):
        if (n%i == 0):
            return False
    return True

num: int = int(input("Enter a number: "))

if (is_prime(num)):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")