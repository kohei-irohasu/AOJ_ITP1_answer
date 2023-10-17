#9_A
W = input()
count = 0
while True:
    T = input()
    if T == 'END_OF_TEXT':
        break
    words = T.lower().split()
    for i in range(len(words)):
        if W == words[i]:
            count += 1
print(count)


#9_B
while True:
    s = input()
    if s == '-':
        break
    m = int(input())
    num = sum([int(input()) for _ in range(m)])
    num %= len(s)  # 総和を文字列の長さで割る
    shuffled = s[num:] + s[:num]  # シャッフルした結果の文字列を作成
    print(shuffled)

#9_C
n = int(input())
t = 0
h = 0

for _ in range(n):
    taro, hanako = input().split()
    
    if taro == hanako:
        t += 1
        h += 1
    elif taro > hanako:
        t += 3
    else:
        h += 3

print(t, h)


#9_D

