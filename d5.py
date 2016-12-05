import operator
from hashlib import md5

def get_hash(string_to_hash):
    return md5(string_to_hash).hexdigest()

def decrypt_outer_password(d_id):
    index = 0
    completed = False
    password = ''
    while not completed:
        current_hash = get_hash(d_id + str(index))
        index += 1
        if not current_hash[0:5] == '00000':
            pass
        else:
            password += current_hash[5]
        if len(password) == 8:
            completed = True
    print password

def decrypt_inner_password(d_id):
    completed = False
    password_dict = {}
    password = ''
    index = 0
    while not completed:
        current_hash = get_hash(d_id + str(index))
        index += 1
        if not current_hash[0:5] == '00000':
            pass
        else:
            try:
                pass_ind = int(current_hash[5])
                if pass_ind < 8:
                    if not pass_ind in password_dict:
                        password_dict[pass_ind] = current_hash[6]
            except ValueError:
                pass
        if len(password_dict) == 8:
            completed = True
    sorted_by_key = sorted(password_dict.items(), key=operator.itemgetter(0))
    for toople in sorted_by_key:
        password += toople[1]
    print password

def main():
    # do test input
    #door_id = 'abc'
    #decrypt_outer_password(door_id)

    # do real input
    #door_id = 'ffykfhsq'
    #decrypt_outer_password(door_id)

    # do test input
    door_id = 'abc'
    decrypt_inner_password(door_id)

    door_id = 'ffykfhsq'
    decrypt_inner_password(door_id)

if __name__ == "__main__":
    
    main()