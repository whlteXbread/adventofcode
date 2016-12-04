import operator

#def load_data(filename: str) -> list:
def load_data_by_rows(filename):
    parsed_data = []
    with open(filename) as data:
        for line in data:
            nums_in_line = [int(x) for x in line.strip().split()]
            parsed_data.append(nums_in_line)
    return parsed_data

def load_data_by_cols(filename):
    parsed_data = []
    with open(filename) as data:
        line_counter = 0
        three_rows = []
        for line in data:
            nums_in_line = [int(x) for x in line.strip().split()]
            three_rows += nums_in_line
            line_counter += 1
            if line_counter == 3:
                line_counter = 0
                for x in range(0, 3):
                    parsed_data.append(three_rows[x::3])
                three_rows = []
    return parsed_data

def is_triangle(side_lengths):
    # check to see if there are only three lengths
    if not len(side_lengths) == 3:
        # raise...
        pass
    side_lengths.sort(reverse=True)
    if not side_lengths[0] < (side_lengths[1] + side_lengths[2]):
        return False
    else:
        return True

def organize_lengths(side_lengths):
    # this function is dumb, for the purpose of this exercise I can just sort :/
    max_length = max(side_lengths)
    max_index = side_lengths.index(max_length)
    ordered = [int] * 3
    ordered[0] = side_lengths[max_index]
    side_lengths.pop(max_index)
    ordered[1] = side_lengths[0]
    ordered[2] = side_lengths[1]
    return ordered


if __name__ == "__main__":
    triangles = load_data_by_rows('d3_input.txt')
    triangle_counter = 0
    for triangle in triangles:
        if is_triangle(triangle):
            triangle_counter += 1
    print triangle_counter

    triangles = load_data_by_cols('d3_input.txt')
    triangle_counter = 0
    for triangle in triangles:
        if is_triangle(triangle):
            triangle_counter += 1
    print triangle_counter