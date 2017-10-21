def convert_to_base(a, b):
    mul = a // b      # floor division, give the multiple of b that a is
    rem = a % b       # mod division, gives the remainder after dividing by b

    if a == 0:
        return '0'
    elif mul == 0:
        return str(rem)
    else:
        return convert_to_base(mul, b) + str(rem)


def answer(n, b):
    # create a list that will store all the IDs
    ids = []
    new_id = n
    length = len(new_id)

    while new_id not in ids:
        # fill in the list with the newest ID
        ids.append(new_id)

        # sort the input ID into a list of asc and desc digits
        digits = list(new_id)
        digits_asc = sorted(digits)
        digits_desc = sorted(digits, reverse=True)

        # convert the strings to numbers
        y = int(''.join(digits_asc), b)
        x = int(''.join(digits_desc), b)

        # subtract the numbers
        z = x - y

        # convert the number to the original base
        temp_id = convert_to_base(z, b)
        print temp_id
        # and fill in the leading zeroes
        new_id = temp_id.zfill(length)

    first = ids.index(new_id)

    ret = len(ids) - first
    # print(ids)
    # print(new_id)
    # print(ret)
    return ret


print answer('1211', 10)
print 5 // 2