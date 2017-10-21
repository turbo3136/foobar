import time
start_time = time.time()

def distance_guess(begin, end):
    ret = 1 + abs(end[0] - begin[0]) + abs(end[1] - begin[1])
    return ret


def index_to_pop(q_weight, q_step):
    min_weight = min(q_weight)
    ind = [i for i, x in enumerate(q_weight) if x == min_weight]
    if len(ind) != 1:
        steps = [q_step[i] for i in ind]
        steps_ind = steps.index(max(steps))
        ret = ind[steps_ind]
    else:
        ret = ind[0]

    return ret


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
    q_weight = [distance_guess(start, end)]


    # create a matrix the size of maze and initialize with 0's
    # we'll use it to track if we've been to a node and if it's with a path thru a wall
    visited = [[0 for j in range(size[y])] for i in range(size[x])]

    """here's the beginning of the loop"""
    while q:
        # find out which index to pop
        ind = index_to_pop(q_weight, q_step)

        # start with the current node and set visited[node[x]][node[y]] = 2 if is_wall_path = 0, else 1
        # Look to see which adjacent nodes are open, based on whether we've been thru a wall or not.
        # Put the open nodes in the queue
        # (it's open if is_wall_path == 0 or maze[node[x]][node[y]] == 0)
        node = q.pop(ind)
        is_wall_path = q_wall.pop(ind)
        step = q_step.pop(ind)
        weight = q_weight.pop(ind)

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
                    q_weight.append(step + distance_guess(new_node, end))

            # if we're not moving past the top or bottom edge, look at the cell
            if 0 <= node[y] + i < size[y]:
                new_node = [node[x], node[y] + i]

                # same logic as above
                if is_wall_path + maze[new_node[x]][new_node[y]] + visited[new_node[x]][new_node[y]] < 2:
                    q.append(new_node)
                    q_wall.append(is_wall_path + maze[new_node[x]][new_node[y]])
                    q_step.append(step + 1)
                    q_weight.append(step + distance_guess(new_node, end))

    """and the end of the loop"""


print answer([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
# print answer([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
# print answer([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
# print answer([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

# print index_to_pop([0, 0, 9], [5, 5, 11])

print("--- %s seconds ---" % (time.time() - start_time))
