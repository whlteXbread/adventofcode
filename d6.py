import operator

def load_data(filename):
    parsed_data = []
    with open(filename, 'r') as data:
        for line in data:
            parsed_data.append(line.strip())
    return parsed_data

def recover_message(message_list):
    message_length = len(message_list[0])
    counter = {}
    for line in message_list:
        for x in range(0,message_length):
            if x not in counter:
                counter[x] = {}
            if line[x] not in counter[x]:
                counter[x][line[x]] = 1
            else:
                counter[x][line[x]] += 1
    message = ''
    for character_number in counter:
        sorted_letters = sorted(counter[character_number].items(), key=operator.itemgetter(1))
        message += sorted_letters[-1][0]
    print(message)

def recover_message_mod(message_list):
    message_length = len(message_list[0])
    counter = {}
    for line in message_list:
        for x in range(0,message_length):
            if x not in counter:
                counter[x] = {}
            if line[x] not in counter[x]:
                counter[x][line[x]] = 1
            else:
                counter[x][line[x]] += 1
    message = ''
    for character_number in counter:
        sorted_letters = sorted(counter[character_number].items(), key=operator.itemgetter(1))
        message += sorted_letters[0][0]
    print(message)

def main():
    test_data = load_data('d6_test_input.txt')
    recover_message(test_data)

    part1_data = load_data('d6_input.txt')
    recover_message(part1_data)

    recover_message_mod(test_data)
    recover_message_mod(part1_data)

if __name__ == "__main__":
    main()