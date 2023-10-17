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
