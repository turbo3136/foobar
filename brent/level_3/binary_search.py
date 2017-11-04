def find_0(bin_str):
    # iterate through bin_str starting from the end to find the first 0
    for i in range(-1, -1 * len(bin_str), -1):
        if bin_str[i] == '0':
            return i


def operate(bin_str):
    # if the string ends in 0, remove the last element and add 1 to count
    # if the string ends in 1, decide if we should add 1 or subtract 1
    #       if len(str) == 2, add 2 to count and end the loop
    #       else, look at the second to last element, if it's 1 add 1, if it's 0 subtract 1
    if bin_str == '1':
        return ''
    # if the string ends in 0, remove the last element and add 1 to count
    elif bin_str[-1] == '0':
        bin_str = bin_str[0:-1]
        return operate(bin_str) + '1'
    # if we get here, that means the string ends in 1
    # if len(bin_str) == 2, add 2 to count
    elif len(bin_str) == 2:
        return '11'
    # find the location of the first 0 so we can decide what to do
    # if it's in the second to last spot, subtract 1 by making the last element '0'
    # and add 1 to count
    elif find_0(bin_str) == -2:
        bin_str = bin_str[0:-1] + '0'
        return operate(bin_str) + '1'
    # if there are no '0's, change bin_str to one longer starting with 1 followed by all '0's
    elif find_0(bin_str) is None:
        z = len(bin_str)
        bin_str = '1' + '0' * z
        return operate(bin_str) + '1'
    # else, add 1 by removing everything up to find_0, changing it to '1'
    # and adding -1 * find_0 to the count
    else:
        z = find_0(bin_str)
        print bin_str
        print z
        neg_z = -1 * z
        print bin_str
        bin_str = bin_str[0:z] + '1'
        print bin_str
        return operate(bin_str) + '1' * neg_z


def answer(n):
    bin_str = str(bin(int(n)))[2:]
    ops = operate(bin_str)
    ret = len(ops)

    return ret


# print binary_converter('100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
# print binary_converter('999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999')
print answer('4')
