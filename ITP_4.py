#4_A
a, b = map(int, input().split())

d = a // b
r = a % b
f = a / b

print("%d %d %.6f" % (d, r, f))


#4_B
import math
r = float(input())
area = math.pi * r ** 2
circumference = 2 * math.pi * r
print("%.6f %.6f" % (area, circumference))


#4_C
while True:
    inputs = input().split()
    a = int(inputs[0])
    op = inputs[1]
    b = int(inputs[2])

    if op == '?':
        break
    if op == '+':
        print(a + b)
    if op == '-':
        print(a - b)
    if op == '*':
        print(a * b)
    if op == '/':
        print(a // b)

#4_D
N = int(input())
A = list(map(int, input().split()))
print(min(A), max(A), sum(A))

        
    