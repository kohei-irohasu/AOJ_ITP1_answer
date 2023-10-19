#10_A
import math
x1, y1, x2, y2 = map(float, input().split())
distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print(f'{distance:.8f}')


#10_B
import math
a, b, C =map(int, input().split())
PI = 3.1415926535
S = a * b / 2 * math.sin(C / 180 * PI)
L = a + b + math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(C / 180 * PI))
h = b * math.sin(C / 180 * PI)

print(f'{S:.8f}')
print(f'{L:.8f}')
print(f'{h:.8f}')


#10_C
import math
n = int(input())

while n != 0:
    s = list(map(float, input().split()))
    mean = sum(s) / n
    variance = sum((mean - x) ** 2 for x in s) / n
    standard_deviation = math.sqrt(variance)
    
    print(f'{standard_deviation:.8f}')
    
    n = int(input())


#10_D
import math
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

d1 = sum(abs(a[i] - b[i]) for i in range(n))
d2 = math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(n)))
d3 = pow(sum(abs(a[i] - b[i]) ** 3 for i in range(n)), 1/3)
d4 = max(abs(a[i] - b[i]) for i in range(n))

print(f'{d1:.8f}')
print(f'{d2:.8f}')
print(f'{d3:.8f}')
print(f'{d4:.8f}')
