addends = {'U': -3,
           'D': 3,
           'L': -1,
           'R': 1}

inst_list = ['ULL',
             'RRDDD',
             'LURDL',
             'UUUUD']

current_value = 5
out_string = ''

for line in inst_list:
    for character in line:
        if ((current_value + addends[character] > 0) and
                (current_value + addends[character] < 10)):
            current_value = current_value + addends[character]
    out_string += str(current_value)

print out_string
