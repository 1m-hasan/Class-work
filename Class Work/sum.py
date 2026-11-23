def add_num(a: int, b: int) -> int:
    return a+b

a: int = int(input("Enter first number:"))
b: int = int(input("Enter second number:"))

result: int = add_num(a, b)

print(f"{a} + {b} = {result}")
