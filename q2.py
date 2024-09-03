def is_fibonacci(n):
    def is_perfect_square(x):
        s = int(x**0.5)
        return s*s == x

    return is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4)


try:
    number = int(input("Inform a number: "))

    if is_fibonacci(number):
        print(f"{number} is in Fibonacci sequence.")
    else:
        print(f"{number} is not in Fibonacci sequence.")

except Exception as e:
    print(e)
