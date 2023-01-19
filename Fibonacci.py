def fibonacci(n):
    if n <= 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib = [0]*n
        fib[0], fib[1] = 0, 1
        for i in range(2, n):
            fib[i] = fib[i-1] + fib[i-2]
        return fib

# test the function
n = 10
print(fibonacci(n))
