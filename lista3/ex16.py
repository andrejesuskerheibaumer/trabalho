a, b = 0, 1

print("Série de Fibonacci até passar de 500:")

while a <= 500:
    print(a, end=" ")
    a, b = b, a + b
