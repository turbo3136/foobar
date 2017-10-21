import time
start_time = time.time()

# valid_step returns -1 for invalid steps or the new value for is_wall_path if valid
def valid_step(maze, x, y, visited, is_wall_path):
    max_x = len(maze) - 1
    max_y = len(maze[0]) - 1

    if x > max_x or y > max_y or x < 0 or y < 0:
        return -1

    elif is_wall_path + maze[x][y] + visited[x][y] < 2:
        return is_wall_path + maze[x][y]

    else:
        return -1


def dfs(maze, x_pos, y_pos, visited, is_wall_path):
    end_x = len(maze) - 1
    end_y = len(maze[0]) - 1

    # if we're one away from the end of the maze, return 2
    if (x_pos == end_x - 1 and y_pos == end_y) or (x_pos == end_x and y_pos == end_y - 1):
        return 2

    # if we haven't gone thru a wall, set visited = 2, else visited = 1
    if is_wall_path == 0:
        visited[x_pos][y_pos] = 2
    else:
        visited[x_pos][y_pos] = 1

    solution_size = 9999

    # East
    check = valid_step(maze, x_pos + 1, y_pos, visited, is_wall_path)
    if check > -1:
        steps = dfs(maze, x_pos + 1, y_pos, visited, check)
        solution_size = steps + 1

    # South
    check = valid_step(maze, x_pos, y_pos + 1, visited, is_wall_path)
    if check > -1:
        steps = dfs(maze, x_pos, y_pos + 1, visited, check)
        if steps + 1 < solution_size:
            solution_size = steps + 1

    # West
    check = valid_step(maze, x_pos - 1, y_pos, visited, is_wall_path)
    if check > -1:
        steps = dfs(maze, x_pos - 1, y_pos, visited, check)
        if steps + 1 < solution_size:
            solution_size = steps + 1

    # North
    check = valid_step(maze, x_pos, y_pos - 1, visited, is_wall_path)
    if check > -1:
        steps = dfs(maze, x_pos, y_pos - 1, visited, check)
        if steps + 1 < solution_size:
            solution_size = steps + 1

    return solution_size


def answer(maze):
    start_x = 0
    start_y = 0
    is_wall_path = 0

    visited = [[0 for j in range(len(maze[0]))] for i in range(len(maze))]

    ret = dfs(maze, start_x, start_y, visited, is_wall_path)

    return ret


# print answer([[0, 0, 0, 0], [0, 0, 0, 0]])
print answer([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
# print answer([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
# print answer([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

print("--- %s seconds ---" % (time.time() - start_time))
