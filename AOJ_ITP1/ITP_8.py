#8_A
ch = input()
ans = ""
for i in ch:
    if i.islower():
        ans += i.upper()
    elif i.isupper():
        ans += i.lower()
    else:
        ans += i
print(ans)

#8_B
while True:
    total = 0
    x = input()
    if x == '0':
        break
    total += sum(int(i) for i in x)
    print(total)
    
    

#8_C
count_table = [0] * 128
while True:
    try:
        ch = input().strip()  #strip()は文字列の先頭と末尾から空白文字（スペース、タブ、改行文字）を削除する
        ch = ch.lower()        
        for i in ch:
            count_table[ord(i)] += 1
    except EOFError:
        break
    
for i in range(97, 123):
    print(f'{chr(i)} : {count_table[i]}')

#8_D
s = input()
p = input()

if p in s * 2:
    print('Yes')
else:
    print('No')
