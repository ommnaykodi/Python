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
