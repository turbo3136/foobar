import time
start_time = time.time()

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
def answer(maze):
    # store a few things to start
    start = [0, 0]
    end = [len(maze) - 1, len(maze[0]) - 1]   # ending position
    size = [len(maze), len(maze[0])]          # maze size for loops
    x = 0
    y = 1

    # create the queue, the queue wall, and queue step
    # q_wall tells us whether the path has been through a wall already
    # q_step will provide our return value, the number of steps the path took
    q = [start]
    q_wall = [0]
    q_step = [0]


    # create a matrix the size of maze and initialize with 0's
    # we'll use it to track if we've been to a node and if it's with a path thru a wall
    visited = [[0 for j in range(size[y])] for i in range(size[x])]

    """here's the beginning of the loop"""
    while q:

        # start with the current node and set visited[node[x]][node[y]] = 2 if is_wall_path = 0, else 1
        # Look to see which adjacent nodes are open, based on whether we've been thru a wall or not.
        # Put the open nodes in the queue
        # (it's open if is_wall_path == 0 or maze[node[x]][node[y]] == 0)
        node = q.pop(0)
        is_wall_path = q_wall.pop(0)
        step = q_step.pop(0)

        if is_wall_path == 0:
            visited[node[x]][node[y]] = 2
        else:
            visited[node[x]][node[y]] = 1

        # if we're at the end of the maze, return the path
        if node == end:
            return step + 1

        # look for all adjacent cells
        for i in [1, -1]:
            # if we're not moving past the left or right edge, look at the cell
            if 0 <= node[x] + i < size[x]:
                new_node = [node[x] + i, node[y]]

                # if is_wall_path + maze + visited < 2, then we'll put that in the queue
                # and set q_wall.append(is_wall_path + maze)
                if is_wall_path + maze[new_node[x]][new_node[y]] + visited[new_node[x]][new_node[y]] < 2:
                    q.append(new_node)
                    q_wall.append(is_wall_path + maze[new_node[x]][new_node[y]])
                    q_step.append(step + 1)

            # if we're not moving past the top or bottom edge, look at the cell
            if 0 <= node[y] + i < size[y]:
                new_node = [node[x], node[y] + i]

                # same logic as above
                if is_wall_path + maze[new_node[x]][new_node[y]] + visited[new_node[x]][new_node[y]] < 2:
                    q.append(new_node)
                    q_wall.append(is_wall_path + maze[new_node[x]][new_node[y]])
                    q_step.append(step + 1)

    """and the end of the loop"""


# print answer([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
# print answer([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
print answer([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

print("--- %s seconds ---" % (time.time() - start_time))
