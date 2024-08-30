def is_fibonacci(n):
    def is_perfect_square(x):
        s = int(x**0.5)
        return s*s == x

    return is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4)

try:
    number = int(input("Informe um número: "))

    if is_fibonacci(number):
        print(f"O número {number} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {number} não pertence à sequência de Fibonacci.")

except Exception as e:
    print(e)