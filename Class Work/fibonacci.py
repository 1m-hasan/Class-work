def fibonacci(n: int) -> int:
    """
    0,1,1,2,3,5,8,13,21
    fibonachhi(n) = (n-2)+(n-1)+n
    """

    if (n==1 or n==2): return n-1

    return fibonacci(n-2) + fibonacci(n-1)

num: int = int(input("Enter a number: "))

fibo: int = fibonacci(num)

print(f"The value of term {num} in the Fibonacci series is {fibo}")