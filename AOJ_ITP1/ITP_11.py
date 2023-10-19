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
