def is_even(n: int) -> bool:
    if (n%2 == 0): return True
    else: return False

n: int = int(input("Enter a number: "))

if (is_even(n)):
    print(f"{n} is a even number")
else:
    print(f"{n} is a odd number")