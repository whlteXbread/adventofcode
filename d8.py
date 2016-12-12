import numpy as np

def load_data(filename):
    parsed_data = []
    with open(filename, 'r') as data:
        for line in data:
            parsed_data.append(line.strip())
    return parsed_data

class BrokenScreen(object):
    def __init__(self, x_dim, y_dim):
        self.x_size = x_dim
        self.y_size = y_dim
        self.screen = np.zeros((y_dim, x_dim))
    def parse_instruction(self, instruction):
        instruction = instruction.split(' ')
        if instruction[0] == 'rect':
            x_y_size = instruction[1].split('x')
            self.generate_rect(int(x_y_size[0]), int(x_y_size[1]))
        elif instruction[0] == 'rotate':
            if instruction[1] == 'row':
                self.rotate_row(int(instruction[2][2:]), int(instruction[4]))
            elif instruction[1] == 'column':
                self.rotate_column(int(instruction[2][2:]), int(instruction[4]))

    def generate_rect(self, x_size, y_size):
        print("making rect {} by {}".format(x_size,y_size))
        self.screen[0:y_size:, 0:x_size:] = 1

    def rotate_row(self, row, offset):
        print("rotating row {} by {}".format(row, offset))
        rotate_slice = self.generate_slice(self.x_size, offset)
        self.screen[(row), 0:self.x_size:] = self.screen[(row), rotate_slice]

    def rotate_column(self, column, offset):
        print("rotating column {} by {}".format(column, offset))
        rotate_slice = self.generate_slice(self.y_size, offset)
        self.screen[0:self.y_size:, (column)] = self.screen[rotate_slice, (column)]

    def generate_slice(self, dim_length, offset):
        if offset == 0:
            raise ValueError("cannot rotate by zero")
        start_point = dim_length - offset
        rotate_slice = (start_point,)
        for x in range(start_point + 1, dim_length):
            rotate_slice += (x,)
        for x in range(0, start_point):
            rotate_slice += (x,)
        return rotate_slice
    
    def num_lit_pixels(self):
        return sum(sum(self.screen))
    
    def __str__(self):
        current_display = 'On Screen: \n'
        for y in range(0, self.y_size):
            for x in range(0, self.x_size):
                if self.screen[y, x]:
                    current_display += '#'
                else:
                    current_display += ' '
            current_display += '\n'
        return current_display

def main():
    instruction_set = load_data('d8_input.txt')
    broken_screen = BrokenScreen(50,6)
    for instruction in instruction_set:
        broken_screen.parse_instruction(instruction)
        print(broken_screen)
    print(broken_screen.num_lit_pixels())

if __name__ == "__main__":
    main()