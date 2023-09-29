def get_neighbors(node, maze):
    neighbors = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

    for dx, dy in directions:
        x, y = node
        new_x, new_y = x + dx, y + dy

        if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] != '#':
            neighbors.append((new_x, new_y))

    return neighbors


def solve_maze_bfs(maze, start):
    queue = []  # Initialize a queue for BFS
    visited = set()  # Keep track of visited nodes
    paths = {}  # Keep track of paths

    # Add starting point to the queue and mark it as visited
    queue.append(start)
    visited.add(start)

    while queue:
        current_node = queue.pop(0)
        i,j = current_node
        if maze[i][j] == 'G':
            # Backtrack to find the solution
            path = []
            while current_node != start:
                path.append(current_node)
                current_node = paths[current_node]
            path.append(start)
            return path[::-1],visited  # return Reversed the path and visited nodes

        # Get neighbors, add them to stack and visited
        for neighbor in get_neighbors(current_node, maze):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                paths[neighbor] = current_node

    return None  # If no solution is found


def solve_maze_dfs(maze, start):
    stack = [] # Initialize a stack for DFS
    visited = set() # Keep track of visited nodes
    paths = {} # Keep track of paths

    # Add starting point to the stack and mark it as visited
    stack.append(start)
    visited.add(start)

    while stack:
        current_node = stack.pop()
        i,j = current_node
        if maze[i][j] == 'G':
            # Backtrack to find the solution
            solution_path = []
            while current_node != start:
                solution_path.append(current_node)
                current_node = paths[current_node]
            solution_path.append(start)
            return solution_path[::-1], visited # Reverse the path

        # Get neighbors, add them to stack and visited
        for neighbor in get_neighbors(current_node, maze):
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
                paths[neighbor] = current_node

    return None     # If no solution


# Maze representation
maze = [['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
        ['#',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S','#'],
        ['#',' ','#',' ','#',' ','#','#','#',' ','#',' ','#','#','#','#','#',' ','#'],
        ['#',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ',' ',' ','#',' ','#',' ','#'],
        ['#','#','#','#','#','#','#',' ','#','#','#','#','#',' ','#',' ','#',' ','#'],
        ['#',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ','#',' ','#'],
        ['#',' ','#',' ','#','#','#','#','#','#','#','#','#','#','#',' ','#',' ','#'],
        ['#',' ','#',' ',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ',' ','#'],
        ['#',' ','#','#','#','#','#','#','#',' ','#',' ','#','#','#','#','#','#','#'],
        ['#',' ',' ',' ',' ',' ','#',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ','#'],
        ['#','#','#','#','#',' ','#',' ','#','#','#','#','#',' ','#','#','#',' ','#'],
        ['#',' ','#',' ',' ',' ','#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ','#'],
        ['#',' ','#',' ','#','#','#','#','#',' ','#',' ','#',' ','#','#','#',' ','#'],
        ['#',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ',' ',' ','#',' ',' ',' ','#'],
        ['#',' ','#','#','#',' ','#',' ','#','#','#',' ','#','#','#',' ','#',' ','#'],
        ['#',' ',' ',' ',' ',' ','#',' ',' ',' ','#',' ',' ',' ','#',' ','#',' ','#'],
        ['#','#','#','#','#','#','#','#','#',' ','#','#','#','#','#',' ','#',' ','#'],
        ['#','G',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' ','#'],
        ['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']]

# Define start coordinates
start = (1, 18)

    
def choose():
    print('enter 1 for BFS algorithm\nenter 2 for DFS algorithm')
    enter = int(input('your choice: '))
    if enter == 1:
        
        # Solve the maze
        solution,visited = solve_maze_bfs(maze, start)

        if solution:
            print("Path found for BFS:")
            for row in range(len(maze)):
                for col in range(len(maze[0])):
                    if (row, col) in solution:
                        print('A', end=' ')
                    elif (row, col) in visited:
                        print('-', end=' ')
                    else:
                        print(maze[row][col], end=' ')
                print()
    else:
        # Solve the maze
        solution,visited = solve_maze_dfs(maze, start)

        if solution:
            print("Path found for DFS:")
            for row in range(len(maze)):
                for col in range(len(maze[0])):
                    if (row, col) in solution:
                        print('A', end=' ')
                    elif (row, col) in visited:
                        print('-', end=' ')
                    else:
                        print(maze[row][col], end=' ')
                print()
choose()