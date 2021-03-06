import time
start_time = time.time()


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
        return 0
    # if the string ends in 0, remove the last element and add 1 to count
    elif bin_str[-1] == '0':
        bin_str = bin_str[0:-1]
        return operate(bin_str) + 1
    # if we get here, that means the string ends in 1
    # if len(bin_str) == 2, add 2 to count
    elif len(bin_str) == 2:
        return 2
    # find the location of the first 0 so we can decide what to do
    # if it's in the second to last spot, subtract 1 by making the last element '0'
    # and add 1 to count
    elif find_0(bin_str) == -2:
        bin_str = bin_str[0:-1] + '0'
        return operate(bin_str) + 1
    # if there are no '0's, change bin_str to one longer starting with 1 followed by all '0's
    elif find_0(bin_str) is None:
        z = len(bin_str)
        bin_str = '1' + '0' * z
        return operate(bin_str) + 1
    # else, add 1 by removing everything up to find_0, changing it to '1'
    # and adding -1 * find_0 to the count
    else:
        z = find_0(bin_str)
        neg_z = -1 * z
        bin_str = bin_str[0:z] + '1'
        return operate(bin_str) + neg_z


def answer(n):
    bin_str = str(bin(int(n)))[2:]
    ret = operate(bin_str)

    return ret


print answer('100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
# print answer('999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999')
# print answer('15')

print("--- %s seconds ---" % (time.time() - start_time))

