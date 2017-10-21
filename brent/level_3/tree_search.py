# use A* tree search algorithm to find the best path through the maze


# create a cost function that finds the distance between
# two points, assuming there's no wall
def distance_guess(x1, y1, x2, y2):
    ret = abs(x2 - x1) + abs(y2 - y1)
    return ret


def path_length(path):
    return len(path)


def answer(maze):
    # start with some values
    start = [0, 0]
    end = [len(maze) - 1, len(maze[0]) - 1]
    size = [len(maze), len(maze[0])]
    x = 0
    y = 1

    # the queue
    q = [start]
    q_wall = [0]
    q_step = [0]
    q_weight = distance_guess(0, 0, end[x], end[y])
    print q_weight
    # the visited
    visited = [[0 for j in range(size[y])] for i in range(size[x])]


print answer([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
# print answer([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
# print answer([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])


