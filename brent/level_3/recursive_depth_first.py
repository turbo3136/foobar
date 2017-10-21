import time
start_time = time.time()


def valid_step(maze, x, y, visited):
    max_x = len(maze) - 1
    max_y = len(maze[0]) - 1

    if x > max_x or y > max_y or x < 0 or y < 0:
        return False

    elif visited[x][y] == 1:
        return False

    elif maze[x][y] == 1:
        return False

    return True


def dfs(maze, x_pos, y_pos, visited):
    end_x = len(maze) - 1
    end_y = len(maze[0]) - 1
    visited[x_pos][y_pos] = 1

    # if we're one away from the end of the maze, return 2
    if (x_pos == end_x - 1 and y_pos == end_y) or (x_pos == end_x and y_pos == end_y - 1):
        return 2

    solution_size = 9999

    # East
    if valid_step(maze, x_pos + 1, y_pos, visited):
        steps = dfs(maze, x_pos + 1, y_pos, visited)
        solution_size = steps + 1

    # South
    if valid_step(maze, x_pos, y_pos + 1, visited):
        steps = dfs(maze, x_pos, y_pos + 1, visited)
        if steps + 1 < solution_size:
            solution_size = steps + 1

    # West
    if valid_step(maze, x_pos - 1, y_pos, visited):
        steps = dfs(maze, x_pos - 1, y_pos, visited)
        if steps + 1 < solution_size:
            solution_size = steps + 1

    # North
    if valid_step(maze, x_pos, y_pos - 1, visited):
        steps = dfs(maze, x_pos, y_pos - 1, visited)
        if steps + 1 < solution_size:
            solution_size = steps + 1

    return solution_size


def answer(maze):
    start_x = 0
    start_y = 0

    visited = [[0 for j in range(len(maze[0]))] for i in range(len(maze))]

    ret = dfs(maze, start_x, start_y, visited)

    return ret


# print answer([[0, 0, 0, 0], [0, 0, 0, 0]])
# print answer([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
print answer([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

print("--- %s seconds ---" % (time.time() - start_time))
