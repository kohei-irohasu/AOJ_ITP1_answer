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
    marks = ['S', 'H', 'C', 'D']
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

