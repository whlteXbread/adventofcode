import re

def load_data(filename):
    parsed_data = []
    with open(filename, 'r') as data:
        for line in data:
            parsed_data.append(line.strip())
    return parsed_data

class ip7_address(object):
    def __init__(self, address):
        # split out any hypernet sequences
        self.address = address
        self.hypernets = self.gather_hypernet_seq()
        self.not_hypernet = self.gather_not_hypernet_seq()

    def gather_hypernet_seq(self):
        hypernet_seq = re.findall(r"\[([^\]]*)\]", self.address)
        return hypernet_seq
    def gather_not_hypernet_seq(self):
        not_hypernet_seq = []
        splittee = self.address
        for h_net in self.hypernets:
            splitted = splittee.split('[' + h_net + ']')
            not_hypernet_seq.append(splitted[0])
            splittee = splitted[1]
        not_hypernet_seq.append(splittee)
        return not_hypernet_seq

    def has_abba(self, test_string):
        for index in range(1, len(test_string) - 1):
            if (index + 1) < len(test_string) and \
               test_string[index] == test_string[index + 1]:
                if not test_string[index] == test_string[index - 1] and \
                   (index + 2) < len(test_string) and \
                   test_string[index - 1] == test_string[index + 2]:
                    return True
            else:
                pass
        return False
    def has_aba(self, test_string):
        index = 0
        aba_list = []
        while index < (len(test_string) - 1):
            if (index + 2) < len(test_string) and \
               test_string[index] == test_string[index + 2]:
                if not test_string[index] == test_string[index + 1]:
                    aba_list.append(test_string[index] + test_string[index + 1] + test_string[index])
                index += 1
            else:
                index += 1
        return aba_list
    def supports_tls(self):
        # check for abba in hypernet sequence
        for seq in self.hypernets:
            abba_time = self.has_abba(seq)
            # if there's one in there ,return False
            if abba_time:
                return False
        # otherwise, check for abba in the rest of the sequence
        for seq in self.not_hypernet:
            abba_time = self.has_abba(seq)
            if abba_time:
                return True
    def supports_ssl(self):
        # check for aba in hypernets
        aba_time = []
        for seq in self.hypernets:
            aba_result = self.has_aba(seq)
            if aba_result:
                for result in aba_result:
                    aba_time.append(result)

        # now check for bab in not_hypernets
        if aba_time:
            for aba in aba_time:
                search_string = aba[1] + aba[0] + aba[1]
                for seq in self.not_hypernet:
                    if search_string in seq:
                        return True
        return False

def main():
    # load the input data
    test_data = load_data('d7_test_input.txt')
    # loop through the inputs and check if they support TLS
    for address in test_data:
        test_obj = ip7_address(address)
        if test_obj.supports_tls():
            print(address + ": HEEEYYYYY")
    # if they do, increment the counter.
    pass

    # load the actual data
    ip_data = load_data('d7_input.txt')
    counter = 0
    for address in ip_data:
        ip_obj = ip7_address(address)
        if ip_obj.supports_tls():
            counter += 1
    print("TLS count: " + str(counter))

    # part 2
    for address in test_data:
        test_obj = ip7_address(address)
        if test_obj.supports_ssl():
            print(address + ": HEEEYYYYY")
    
    counter = 0
    for address in ip_data:
        ip_obj = ip7_address(address)
        if ip_obj.supports_ssl():
            counter += 1
    print("SSL count: " + str(counter))

if __name__ == "__main__":
    main()
