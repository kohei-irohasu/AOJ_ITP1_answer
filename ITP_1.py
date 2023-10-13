#1_A
print("Hello World")

#1_B
N = int(input)
print(N ** 3)

#1_C
a, b = map(int, input().split())
s = a * b
l = 2 * a + 2 * b
print(s, l)

#1_D
S = int(input())
h = S // 3600
m = S % 3600 // 60
S = S % 60
print(f'{h}:{m}:{s}')
