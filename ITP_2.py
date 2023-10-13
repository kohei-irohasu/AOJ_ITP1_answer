#2_A
a, b = int(input().split())

if a < b:
    print("a < b")
elif a > b:
    print("a > b")
else:
    print("a == b")

#2_B
a, b, c = map(int, input().split())

if a < b and b < c:
    print("Yes")
else:
    print("No")

#2_C
a, b, c = map(int, input().split())

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(a, b, c)

#2_D
W, H, x, y, r = map(int, input().split())

if r <= x and x <= W - r and r <= y and y <= H - r:
    print("Yes")
else:
    print("No")

