#5_A
while True:
    h, w = map(int, input().split())
    
    if h == 0 and w == 0:
        break
    for i in range(h):
        print('#' * w)
    
    print()

#5_B
while True:
    h, w = map(int, input().split())
    
    if h == 0 and w == 0:
        break
    
    for i in range(h):
        for j in range(w):
            if i == 0 or i + 1 == h or j == 0 or j + 1 == w:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()
    
#5_C
while True:
    h, w = map(int, input().split())
    
    if h == 0 and w == 0:
        break
    
    for i in range(h):
        for j in range(w):
            if i % 2 == 0:
                print('#' if j % 2 == 0 else '.', end='')
            else:
                print('.' if j % 2 == 0 else '#', end='')
        print()
    print()

#5_C 別解（i,jの偶奇が一致してるかどうかで場合分け）
while True:
    h, w = map(int, input().split())
    
    if h == 0 and w == 0:
        break
    
    for i in range(h):
        for j in range(w):
            if (i + j) % 2 == 0:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()
    

#5_D
n = int(input())
ans = []
for i in range(1, n + 1):
    x = i
    if x % 3 == 0:
        ans.append(i)
        continue
    while x: # xが0になったらFalse
        if x % 10 == 3:
            ans.append(i)
            break
        x //= 10
print(*ans)
