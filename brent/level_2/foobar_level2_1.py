def answer(s):
    # remove all hyphens
    s = s.replace('-', '')

    # split the string into a list
    s_list = list(s)

    # store a few important variables
    right_char = '>'
    ret = 0

    # find the index for each right and left facing person
    right_pos = []
    left_pos = []
    for i, x in enumerate(s_list):
        if x == right_char:
            right_pos.append(i)
        else:
            left_pos.append(i)

    # now that we have the positions of R and L,
    # find how many Ls are at an index greater than each R
    for i in right_pos:     # loop through R positions
        for j in left_pos:      # loop through L positions
            if j > i:
                ret += 1        # every time an L is at an index greater than R, add 1 to ret

    return ret * 2


print answer('>>>>>>>>>>>>>>>>>>>><')
