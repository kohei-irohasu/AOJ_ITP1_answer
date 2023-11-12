#4_A
a, b = map(int, input().split())
d = a // b
r = a % b
f = a / b
print(f'{d} {r} {f:.8f}')


#4_B
import math
PI = math.pi
r = float(input())
area = PI*r**2
circumferrence = 2*PI*r
print(f'{area:.8f} {circumferrence:.8f}')


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

        
    