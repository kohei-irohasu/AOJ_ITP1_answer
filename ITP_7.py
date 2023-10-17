#7_A
while True:
    m, f, r = map(int, input().split())
    if m == -1 and f == -1 and r == -1:
        break
    if m == -1 or f == -1:
        grade = 'F'
    elif m + f >= 80:
        grade = 'A'
    elif m + f >= 65:
        grade = 'B'
    elif m + f >= 50:
        grade = 'C'
    elif m + f >= 30:
        grade = 'C' if r >= 50 else 'D'
    else:
        grade = 'F'
    print(grade)


#7_B
while True:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break
    
    count = 0
    for i in range(1, x // 3 + 1):
        for j in range(i + 1, min(x - (i * 2), n)):
            if x - (i + j) <= n and j < x - (i + j): 
                count += 1
    print(count)


#7_C
r, c = map(int, input().split())
table = [[0] *(c + 1) for _ in range(r + 1)]

for i in range(r):
    row_values = list(map(int, input().split()))
    for j in range(c):
        table[i][j] = row_values[j]
        table[i][c] += row_values[j]
        table[r][j] += row_values[j]

for i in range(c):
    table[r][c] += table[r][i]

for i in table:
    print(*i)


#7_D
n, m, l = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(m)]

C = [[0] * l for _ in range(n)]
for i in range(n):
    for k in range(l):
        for j in range(m):
            C[i][k] += A[i][j] * B[j][k] 

for i in C:
    print(*i)   


        
