# def step(map, x0, y0, x1, y1):        # function to find which cells are open to step to
#     w = len(map[0])

def answer(map):
    # store a few variables
    p0 = [0, 0]     # starting position
    end = [len(map), len(map[0])]       # ending position, or width and height + 1
    best = sum(end) - 1

    # also create the horizontal and vertical connection matrices
    h = [[0] * end[1] for _ in range(end[0] - 1)]
    # loop through the map and note which points have connections (horizontally)
    for y in range(end[1]):
        for x in range(end[0] - 1):
            if map[x][y] == 0 and map[x + 1][y] == 0:
                h[x][y] = 1     # this means x,y connects to x+1,y if h[x][y] = 1
                                # basically, if cell x,y connects to its right, h[x][y] = 1

    # the vertical
    v = [[0] * (end[1] - 1) for _ in range(end[0])]
    # loop through the map and note which points have connections (horizontally)
    for y in range(end[1] - 1):
        for x in range(end[0]):
            if map[x][y] == 0 and map[x][y + 1] == 0:
                v[x][y] = 1

    # now instead create a connection matrix conn, that's 3D
    conn = [[[0 for z in range(2)] for y in range(end[1])] for x in range(end[0])]

    # loop through the map and note which points have connections horizontally and vertically
    for y in range(end[1]):
        for x in range(end[0]):
            if x != end[0] - 1:
                if map[x][y] == 0 and map[x + 1][y] == 0:
                    conn[x][y][0] = 1
            if y != end[1] - 1:
                if map[x][y] == 0 and map[x][y + 1] == 0:
                    conn[x][y][1] = 1


    # print h[1][0]
    # print conn for visualization
    for y in range(0, end[1]):
        s = ''
        for x in range(0, end[0]):
            s += str(conn[x][y]) + '\t'
        print s
    print

    # print v for visualization
    # for y in range(0, end[1] - 1):
    #     s = ''
    #     for x in range(0, end[0]):
    #         s += str(v[x][y]) + '\t'
    #     print s
    # print

    # print the map for visualization
    for y in range(0, end[1]):
        s = ''
        for x in range(0, end[0]):
            s += str(map[x][y]) + '\t'
        print s




# answer([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
answer([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
