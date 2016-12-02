directions = ['L2', 'L3', 'L3', 'L4', 'R1', 'R2', 'L3', 'R3', 'R3', 'L1', 'L3', 'R2', 'R3', 'L3', 'R4', 'R3', 'R3', 'L1', 'L4', 'R4', 'L2', 'R5', 'R1', 'L5', 'R1', 'R3', 'L5', 'R2', 'L2', 'R2', 'R1', 'L1', 'L3', 'L3', 'R4', 'R5', 'R4', 'L1', 'L189', 'L2', 'R2', 'L5', 'R5', 'R45', 'L3', 'R4', 'R77', 'L1', 'R1', 'R194', 'R2', 'L5', 'L3', 'L2', 'L1', 'R5', 'L3', 'L3', 'L5', 'L5', 'L5', 'R2', 'L1', 'L2', 'L3', 'R2', 'R5', 'R4', 'L2', 'R3', 'R5', 'L2', 'L2', 'R3', 'L3', 'L2', 'L1', 'L3', 'R5', 'R4', 'R3', 'R2', 'L1', 'R2', 'L5', 'R4', 'L5', 'L4', 'R4', 'L2', 'R5', 'L3', 'L2', 'R4', 'L1', 'L2', 'R2', 'R3', 'L2', 'L5', 'R1', 'R1', 'R3', 'R4', 'R1', 'R2', 'R4', 'R5', 'L3', 'L5', 'L3', 'L3', 'R5', 'R4', 'R1', 'L3', 'R1', 'L3', 'R3', 'R3', 'R3', 'L1', 'R3', 'R4', 'L5', 'L3', 'L1', 'L5', 'L4', 'R4', 'R1', 'L4', 'R3', 'R3', 'R5', 'R4', 'R3', 'R3', 'L1', 'L2', 'R1', 'L4', 'L4', 'L3', 'L4', 'L3', 'L5', 'R2', 'R4', 'L2']

#directions = ['R5', 'L5', 'R5', 'R3']
#directions = ['R8', 'R4', 'R4', 'R8']

dir_finder = {'north': {'L': 'west', 'R': 'east'},
              'east': {'L': 'north', 'R': 'south'},
              'south': {'L': 'east', 'R': 'west'},
              'west': {'L': 'south', 'R': 'north'}}
mult_finder = {'north': {'L': [-1, 0], 'R': [1, 0]},
               'east': {'L': [0, 1], 'R': [0, -1]},
               'south': {'L': [1, 0], 'R': [-1, 0]},
               'west': {'L': [0, -1], 'R': [0, 1]}}

x = 0
y = 0
direction = 'north'
location_list = []
location_list.append([x,y])
for instruction in directions:
    left_or_right = instruction[0]
    length = int(instruction[1:])
    this_mult = mult_finder[direction][left_or_right]
    for q in range(0,length):
        x = x + (1 * this_mult[0])
        y = y + (1 * this_mult[1])
        if [x,y] in location_list:
            print "eb hq coords: " + str(x) + ", " + str(y)
            print abs(x) + abs(y)
        location_list.append([x,y])
    direction = dir_finder[direction][left_or_right]


print abs(x) + abs(y)
