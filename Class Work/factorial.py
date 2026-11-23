def factorial(n: int) -> int:
    if (n==0 or n==1):
        return 1
    return n * factorial(n-1)

num: int = int(input("Enter a number: "))

fact: int = factorial(num)

print(f"The factorial of {num} is {fact}")