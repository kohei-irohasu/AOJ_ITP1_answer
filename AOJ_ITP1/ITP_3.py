#3_A
for i in range(1000):
    print("Hello World")


#3_B
i = 0
while True:
    x = int(input())
    if x == 0:
        break
    i += 1
    print(f"Case {i}: {x}")


#3_C
while True:
    x, y = map(int, input().split())
    
    if x == 0 and y == 0:
        break
    if x > y:
        print(f'{y} {x}')
    else:
        print(f'{x} {y}')

#3_D
a, b, c = map(int, input().split())

count = 0
for i in range(a, b + 1):
    if c % i == 0:
        count += 1
print(count)

        

