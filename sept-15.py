print("Factorial using While Loop (Increment)")
n = int(input("Enter a number: "))
fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1

print("Factorial =", fact)

print("Factorial using While Loop (Decrement)")
n = int(input("Enter a number: "))
fact = 1
i = n

while i >= 1:
    fact *= i
    i -= 1

print("Factorial =", fact)

print("Factorial using For Loop (Increment)")
n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)

print("Factorial using For Loop (Decrement)")
n = int(input("Enter a number: "))
fact = 1

for i in range(n, 0, -1):
    fact *= i

print("Factorial =", fact)

print("Factorial using Do–While Loop (Python doesn’t have do–while, but we can simulate it)")

n = int(input("Enter a number: "))
fact = 1
i = 1

if n == 0:  # 0! = 1
    print("Factorial = 1")
else:
    while True:
        fact *= i
        i += 1
        if i > n:
            break
    print("Factorial =", fact)
