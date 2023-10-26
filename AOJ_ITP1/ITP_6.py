#6_A
n = int(input())
A = list(map(int, input().split()))

reversed_A = reversed(A)
print(*reversed_A)


#6_B
def find_cards(n, data):
    marks = {'S': [0] * 14, 'H': [0] * 14, 'C': [0] * 14, 'D': [0] * 14}
    
    for i in range(n):
        mark, num = data[i]
        num = int(num)
        marks[mark][num] = 1
    
    for mark in ['S', 'H', 'C', 'D']:
        for num in range(1, 14):
            if marks[mark][num] == 0:
                print(f'{mark} {num}')

n = int(input())
data = [input().split() for _ in range(n)]
find_cards(n, data)    


#6_C
def output(H):
    for row in H:
        print(' ', end='')
        print(*row)

H = [[[0] * 10 for _ in range(3)] for _ in range(4)]
n = int(input())
for _ in range(n):
    h_num, f_num, r_num, div_num = map(int, input().split())
    H[h_num - 1][f_num - 1][r_num - 1] += div_num

for i in range(4):
    output(H[i])
    if i < 3:
        print("#" * 20)
        


#6_D
n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
b = [int(input()) for _ in range(m)]

for row in A:
    result = sum(x * y for x, y in zip(row, b))
    print(result)
    
#zip関数について
# a = [1, 2, 3]
# b = ['a', 'b', 'c']
# zipped = zip(a, b)
# zipped --> [(1, 'a'), (2, 'b'), (3, 'c')]


