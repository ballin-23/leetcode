def fib(n):
    # base case
    if n == 1 or n == 0:
        return 1
    else:
        return fib(n-1) + fib(n-2)


x = fib(3)
print(x)