import operator

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def load_data(filename):
    parsed_data = []
    with open(filename, 'r') as data:
        for line in data:
            parsed_data.append(line.strip())
    return parsed_data

def read_checksum(room_string):
    split_string = room_string.split('[')
    return split_string[1][:-1]

def read_sector_id(room_string):
    split_string = room_string.split('-')
    id_and_checksum = split_string[-1].split('[')
    return int(id_and_checksum[0])

def read_name(room_string):
    split_string = room_string.split('-')
    return split_string[0:-1]

def calculate_checksum(room_name):
    letter_counts = {}
    clean_string = ''.join(room_name)
    for char in clean_string:
        if not char in letter_counts:
            letter_counts[char] = 1
        else:
            letter_counts[char] += 1
    # okay, so I think if you sort alphabetically and then by count the result will be correct
    sorted_by_alpha = sorted(letter_counts.items(), key=operator.itemgetter(0))
    sorted_by_count = sorted(sorted_by_alpha, key=lambda tup: tup[1], reverse=True)
    checksum = ''
    for x in range(0, 5):
        checksum += sorted_by_count[x][0]
    return checksum

def is_decoy(room_string):
    room_name = read_name(room_string)
    if calculate_checksum(room_name) == read_checksum(room_string):
        return False
    else:
        return True

def sum_real_sectors(room_list):
    test_sum = 0
    for room in room_list:
        if not is_decoy(room):
            test_sum += read_sector_id(room)
    return test_sum

def decrypted_name(room_name, sector):
    char_offset = sector % len(ALPHABET)
    decrypted_words = []
    for word in room_name:
        decrypted_word = []
        for char in word:
            char_index = ALPHABET.index(char)
            new_index = char_index + char_offset
            if new_index > (len(ALPHABET) - 1):
                new_index = new_index - len(ALPHABET)
            decrypted_word += ALPHABET[new_index]
        decrypted_words.append(''.join(decrypted_word))
    return ' '.join(decrypted_words)

def find_north_pole(room_list):
    for room in room_list:
        if not is_decoy(room):
            sector = read_sector_id(room)
            room_name = read_name(room)
            room_name = decrypted_name(room_name, sector)
            if 'northpole' in room_name:
                return sector
    

if __name__ == "__main__":
    test_data = load_data('d4_test_input.txt')
    print sum_real_sectors(test_data)

    all_rooms = load_data('d4_input.txt')
    print sum_real_sectors(all_rooms)

    # part 2
    #decrypted_name(['qzmt','zixmtkozy','ivhz'],343)
    print find_north_pole(all_rooms)