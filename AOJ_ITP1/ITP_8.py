#8_A
ch = input()
result = ""
for i in ch:
    if i.islower():
        result += i.upper()
    elif i.isupper():
        result += i.lower()
    else:
        result += i
        
print(result)


#8_B
total = 0
while True:
    line = input()
    if line == '0':
        break
    total += sum(int(i) for i in line)
    print(total)
    total = 0
    

#8_C
count_table = [0] * 256

while True:
    try:
        ch = input().strip()
        for i in ch:
            count_table[ord(i)] += 1
    except EOFError:
        break

for i in range(97, 123):
    ans = count_table[i] + count_table[i - 32]
    print(f'{chr(i)} : {ans}')


#8_D
s = input()
p = input()

if p in s * 2:
    print('Yes')
else:
    print('No')
