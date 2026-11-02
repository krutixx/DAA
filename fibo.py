# Recursive Fibonacci
def fibonacci_recursive(n):
    if n <= 1:
        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Non-recursive Fibonacci
def fibonacci_nonrecursive(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


n = int(input("Enter number of terms: "))

print("Recursive:")
for i in range(n):
    print(fibonacci_recursive(i), end=" ")

print("\nNon-Recursive:")
fibonacci_nonrecursive(n)