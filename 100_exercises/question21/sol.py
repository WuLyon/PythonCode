# Question: A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
# The trace of robot movement is shown as the following: UP 5 DOWN 3 LEFT 3 RIGHT 2 ¡­ The numbers after the direction are steps. 
# Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer. 
# Example: If the following tuples are given as input to the program: UP 5 DOWN 3 LEFT 3 RIGHT 2 Then, the output of the program should be: 2

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

import sys
import math
pos = {'x': 0, 'y': 0}
while True:
    s = input()
    if not s:
        break
    move = s.split()
    if move[0] == 'UP':
        pos['y'] += int(move[1])
    elif move[0] == 'DOWN':
        pos['y'] -= int(move[1])
    elif move[0] == 'LEFT':
        pos['x'] -= int(move[1])
    elif move[0] == 'RIGHT':
        pos['x'] += int(move[1])
    else:
        print('WRONG MOVEMENT!')
        sys.exit(1)

distance = round(math.sqrt(pos['x']**2 + pos['y']**2))
print(type(distance))
