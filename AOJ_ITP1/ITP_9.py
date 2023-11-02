#9_A
W = input()
count = 0

while True:
    T = input()
    if T == 'END_OF_TEXT':
        break
    
    words = T.lower().split()
    for i in words:
        if i == W:
            count += 1
print(count)


#9_B
while True:
    words = input()
    if words == "-":
        break
    
    m = int(input())
    h = sum([int(input()) for _ in range(m)])
    num = h % len(words) # 総和を文字列の長さで割る
    print(words[num:] + words[:num]) # シャッフルした結果の文字列を作成


#9_C
n = int(input())
t_point = 0
h_point = 0

for _ in range(n):
    taro, hanako = input().split()
    
    if taro == hanako:
        t_point += 1
        h_point += 1
    elif taro > hanako:
        t_point += 3
    else:
        h_point += 3
print(t_point, h_point)
    


#9_D
words = input()
q = int(input())

for _ in range(q):
    operation, *args = input().split()
    a, b = int(args[0]), int(args[1])
    if operation == "replace":
        s = args[2]
        words = words[:a] + s + words[b + 1:]
    elif operation == "reverse":
        words = words[:a] + words[a:b + 1][::-1] + words[b + 1:]
    else:
        print(words[a:b + 1])
    
