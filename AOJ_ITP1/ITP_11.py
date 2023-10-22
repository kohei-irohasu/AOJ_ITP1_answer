#11_A
class Dice:
    
    def __init__(self, sides):
        self.sides = sides
        
    def roll(self, direction):
        if direction == 'E':
            (self.sides[0], self.sides[2], self.sides[3], self.sides[5]) = (self.sides[3], self.sides[0], self.sides[5], self.sides[2])
        elif direction == 'W':
            (self.sides[0], self.sides[2], self.sides[3], self.sides[5]) = (self.sides[2], self.sides[5], self.sides[0], self.sides[3])
        elif direction == 'S':
            (self.sides[0], self.sides[1], self.sides[4], self.sides[5]) = (self.sides[4], self.sides[0], self.sides[5], self.sides[1])
        elif direction == 'N':
            (self.sides[0], self.sides[1], self.sides[4], self.sides[5]) = (self.sides[1], self.sides[5], self.sides[0], self.sides[4])
    
    def top(self):
        return self.sides[0]
    
initial_sides = list(map(int, input().split()))
d = Dice(initial_sides)

operations = input()
for i in operations:
    d.roll(i)
print(d.top())


#11_B
class Dice:
    
    def __init__(self, sides):
        self.sides = sides
        
    def roll(self, direction):
        if direction == 'E':
            (self.sides[0], self.sides[2], self.sides[3], self.sides[5]) = (self.sides[3], self.sides[0], self.sides[5], self.sides[2])
        elif direction == 'W':
            (self.sides[0], self.sides[2], self.sides[3], self.sides[5]) = (self.sides[2], self.sides[5], self.sides[0], self.sides[3])
        elif direction == 'S':
            (self.sides[0], self.sides[1], self.sides[4], self.sides[5]) = (self.sides[4], self.sides[0], self.sides[5], self.sides[1])
        elif direction == 'N':
            (self.sides[0], self.sides[1], self.sides[4], self.sides[5]) = (self.sides[1], self.sides[5], self.sides[0], self.sides[4])
        elif direction == 'R': # topを固定で横回転する
            (self.sides[1], self.sides[2], self.sides[3], self.sides[4]) = (self.sides[2], self.sides[4], self.sides[1], self.sides[3])
            
    def top(self):
        return self.sides[0]
    
    def left(self):
        return self.sides[3]
    
    def right(self):
        return self.sides[2]
    
    def front(self):
        return self.sides[1]
    
    
initial_sides = list(map(int, input().split()))
d = Dice(initial_sides)
n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    if d.left() == a:
        d.roll('E')
    if d.right() == a:
        d.roll('W')
    while d.top() != a:
        d.roll('N')
    while d.front() != b:
        d.roll('R')
    print(d.right())
    

#11_C
class Dice:
    
    def __init__(self, sides):
        self.sides = sides
        
    def roll(self, direction):
        if direction == 'E':
            (self.sides[0], self.sides[2], self.sides[3], self.sides[5]) = (self.sides[3], self.sides[0], self.sides[5], self.sides[2])
        elif direction == 'W':
            (self.sides[0], self.sides[2], self.sides[3], self.sides[5]) = (self.sides[2], self.sides[5], self.sides[0], self.sides[3])
        elif direction == 'S':
            (self.sides[0], self.sides[1], self.sides[4], self.sides[5]) = (self.sides[4], self.sides[0], self.sides[5], self.sides[1])
        elif direction == 'N':
            (self.sides[0], self.sides[1], self.sides[4], self.sides[5]) = (self.sides[1], self.sides[5], self.sides[0], self.sides[4])
        elif direction == 'R':
            (self.sides[1], self.sides[2], self.sides[3], self.sides[4]) = (self.sides[2], self.sides[4], self.sides[1], self.sides[3])
            
    def is_equal(self, other):
        return self.sides == other.sides
    
dice1 = Dice(list(map(int, input().split())))
dice2 = Dice(list(map(int, input().split())))
is_same = False

for _ in range(4):
    dice2.roll('R')
    for _ in range(4):
        dice2.roll('N')
        if dice1.is_equal(dice2):
            is_same = True

dice2.roll('E')
for _ in range(4):
        dice2.roll('N')
        if dice1.is_equal(dice2):
            is_same = True
            
dice2.roll('W')
dice2.roll('W')
for _ in range(4):
        dice2.roll('N')
        if dice1.is_equal(dice2):
            is_same = True

if is_same:
    print('Yes')
else:
    print('No')


#11_D
class Dice:
    
    def __init__(self, sides):
        self.sides = sides
        
    def roll(self, direction):
        if direction == 'E':
            (self.sides[0], self.sides[2], self.sides[3], self.sides[5]) = (self.sides[3], self.sides[0], self.sides[5], self.sides[2])
        elif direction == 'W':
            (self.sides[0], self.sides[2], self.sides[3], self.sides[5]) = (self.sides[2], self.sides[5], self.sides[0], self.sides[3])
        elif direction == 'S':
            (self.sides[0], self.sides[1], self.sides[4], self.sides[5]) = (self.sides[4], self.sides[0], self.sides[5], self.sides[1])
        elif direction == 'N':
            (self.sides[0], self.sides[1], self.sides[4], self.sides[5]) = (self.sides[1], self.sides[5], self.sides[0], self.sides[4])
        elif direction == 'R':
            (self.sides[1], self.sides[2], self.sides[3], self.sides[4]) = (self.sides[2], self.sides[4], self.sides[1], self.sides[3])
    
def is_equal(dice1, dice2):
    return dice1.sides == dice2.sides
    
def is_same(dice1, dice2):
    for _ in range(4):
        dice2.roll('R')
        for _ in range(4):
            dice2.roll('N')
            if is_equal(dice1, dice2):
                return True

    dice2.roll('E')
    for _ in range(4):
            dice2.roll('N')
            if is_equal(dice1, dice2):
                return True 
                
    dice2.roll('W')
    dice2.roll('W')
    for _ in range(4):
            dice2.roll('N')
            if is_equal(dice1, dice2):
                return True
    
    return False

n = int(input())
dices = []

for i in range(n):
    sides = list(map(int, input().split()))
    dices.append(Dice(sides))
    
flag = True
for j in range(n - 1):
    for k in range(j + 1, n):
        if is_same(dices[j], dices[k]):
            flag = False
            break

print('Yes' if flag else 'No')
    