"""
    So... we're going to use a breadth first search algorithm, which
    takes one step in each possible direction before going to the next step.
    That means it's guaranteed to find the shortest path first. But ours
    is complicated by the fact that we can remove a wall. Normally, you store
    which cells have been visited and which cells are in the queue to be
    checked next. For us, we'll have to add another parameter to the visited
    list that checks if it's been visited by a path that's removed a wall
    or if it's been visited by a path that hasn't. It's possible to be in a
    cell that's a dead end for a path that's already removed one wall, but
    it's not a dead end for a path that has removed no walls.
"""
def answer(map):
    # store a few things to start
    start = [0, 0]
    end = [len(map) - 1, len(map[0]) - 1]   # ending position
    size = [len(map), len(map[0])]          # map size for loops
    x = 0
    y = 1
    new_node = []

    # create the queue
    q = [[[start, 0]]]

    # create the visited list
    visited = []
    # visited[0] will be the list of node and is_wall_path flag
    # e.g. for the start, visited[0] == [[0, 0], 0]
    # visited[0][0] == node == [0, 0] and visited[0][1] == is_wall_path == 0
    # if is_wall_path == 0, we don't look at it bc a shorter path that
    # hasn't removed walls has already been there before
    # visited.append([[0, 0], 0])
    # print visited[0]

    """here's the beginning of the loop"""

    # start with the current node and look to see which adjacent nodes are open.
    # Put those nodes in the queue and visited.append(node, is_wall_path)
    l = q.pop(0)
    node = l[0][0]
    is_wall_path = l[0][1]
    # print node
    # print is_wall_path

    # if we're at the end of the maze, return the path
    if node == end:
        return path

    # look for all adjacent cells
    for i in [-1, 1]:
        # if we're not moving past the left or right edge, look at the cell
        if 0 <= node[x] + i < size[x]:
            new_node = [node[x] + i, node[y]]
            print new_node
            print map[new_node[x]][new_node[y]]
            # if the new cell == 0 or is a wall but is_wall_path = 0,
            # then add the cell to the queue
            if map[new_node[x]][new_node[y]] == 0:
                q.append([[new_node[x], new_node[y]], is_wall_path])
                print q
            elif is_wall_path == 0:
                q.append([[new_node[x], new_node[y]], 1])
                print q
        # if we're not moving past the top or bottom edge, look at the cell
        if 0 <= node[y] + i < size[y]:
            new_node = [node[x], node[y] + i]
            print new_node
            print map[new_node[x]][new_node[y]]
            # same check as above
            if map[new_node[x]][new_node[y]] == 0:
                q.append([[new_node[x], new_node[y]], is_wall_path])
                print q
            elif is_wall_path == 0:
                q.append([[new_node[x], new_node[y]], 1])
                print q

    """and the end of the loop"""


    # print the map for visualization
    for j in range(size[y]):
        s = ''
        for i in range(size[x]):
            s += str(map[i][j]) + '\t'
        print s


answer([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
# answer([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
