def get_largest(a: int, b: int) -> int:
    if (a > b):
        return a
    return b

num1: int = int(input("Enter first number: "))
num2: int = int(input("Enter second number: "))

largest: int = get_largest(num1, num2)

print(f"The largest number is {largest}")