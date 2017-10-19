# def step(map, x0, y0, x1, y1):        # function to find which cells are open to step to
#     w = len(map[0])

def answer(map):
    # store a few variables
    p0 = [0, 0]     # starting position
    end = [len(map), len(map[0])]       # ending position, or width and height + 1
    best = sum(end) - 1
    hor = 0
    ver = 1

    # now create a connection matrix conn, that's 3D
    conn = [[[0 for z in range(2)] for y in range(end[ver])] for x in range(end[hor])]

    # loop through the map and note which points have connections horizontally and vertically
    for y in range(end[ver]):
        for x in range(end[hor]):
            if x != end[hor] - 1:
                if map[x][y] == 0 and map[x + 1][y] == 0:
                    conn[x][y][hor] = 1
            if y != end[ver] - 1:
                if map[x][y] == 0 and map[x][y + 1] == 0:
                    conn[x][y][ver] = 1

    # print conn for visualization
    for y in range(0, end[ver]):
        s = ''
        for x in range(0, end[hor]):
            s += str(conn[x][y]) + '\t'
        print s
    print

    # print the map for visualization
    for y in range(0, end[ver]):
        s = ''
        for x in range(0, end[hor]):
            s += str(map[x][y]) + '\t'
        print s




# answer([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
answer([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
