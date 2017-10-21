def answer(l, t):
    # find the max value of l
    mx = max(l)
    # and find out how many multiples of the max value t is (rounded up)
    mul = int(-1 * (float(-t)//mx))     # // is floor division (truncate) which always rounds more negative

    # find the length of l and add 1
    stop = len(l) + 1

    # loop through the starting and ending indexes
    for i in range(0, stop - mul):
        for j in range(i + mul, stop):
            s = sum(l[i:j])

            # print str(i) + '\t' + str(j)
            print str(i) + '\t' + str(j) + '\t' + str(s)

            if s == t:
                return [i, j - 1]

    return [-1, -1]


print answer([4, 3, 10, 2, 8], 12)
