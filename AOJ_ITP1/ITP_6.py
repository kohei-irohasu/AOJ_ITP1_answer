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


