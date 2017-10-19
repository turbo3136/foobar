# use a tree search algorithm to find the best path through the maze
"""
Okay, so what I really want to do is use a Breadth First Search to find the
shortest path through the maze, but use a two-level queue in order to track
whether the cell has been visited by a path that has already removed a wall
or if it's been visited by a path that hasn't removed a wall.
"""