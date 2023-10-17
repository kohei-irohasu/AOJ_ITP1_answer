#6_A
n = int(input())
A = list(map(int, input().split()))

reversed_A = reversed(A)
print(*reversed_A)


#6_B
def output(array, mark):
    for i in range(1, 14):
        if array[i] == 0:
            print(f'{mark} {i}')

def main():
    s, h, c, d = [0] * 14, [0] * 14, [0] * 14, [0] * 14
    
    n = int(input())
    
    for _ in range(n):
        mark, tmp = input().split()
        tmp = int(tmp)
        
        if mark == 'S':
            s[tmp] = 1
        elif mark == 'H':
            h[tmp] = 1
        elif mark == 'C':
            c[tmp] = 1
        else:
            d[tmp] = 1

    output(s, 'S')
    output(h, 'H')
    output(c, 'C')
    output(d, 'D')
    
main()


#6_C
def output(H):
    for i in range(3):
        for j in range(10):
            print(f' {H[i][j]}', end='')
        print()
        
def main():
    H1 = [[0] * 10 for _ in range(3)]
    H2 = [[0] * 10 for _ in range(3)]
    H3 = [[0] * 10 for _ in range(3)]
    H4 = [[0] * 10 for _ in range(3)]
    
    n = int(input())
    for _ in range(n):
        h_num, f_num, r_num, div_num = map(int, input().split())
        
        if h_num == 1:
            H1[f_num - 1][r_num - 1] += div_num
        elif h_num == 2:
            H2[f_num - 1][r_num - 1] += div_num
        elif h_num == 3:
            H3[f_num - 1][r_num - 1] += div_num
        else:
            H4[f_num - 1][r_num - 1] += div_num
            
    output(H1)
    print('#' * 20)
    output(H2)
    print('#' * 20)
    output(H3)
    print('#' * 20)
    output(H4)
    

main()

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


