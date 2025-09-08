import math

n = int(input("Enter the value of n:"))

result = 0

for i in range(1, n + 1):
    result += i/math.factorial(i)

print("Sum of series =", result)