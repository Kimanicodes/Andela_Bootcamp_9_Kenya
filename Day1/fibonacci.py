def fibonacci(n):
    a = 0
    b = 1
    fibonacci_sequence = [a, b]
    while b < n:
        a, b = b, a + b
        fibonacci_sequence.append(b)
    return fibonacci_sequence

print(fibonacci(50))
