'''def findAllWays(x, y, matrix, N, path, visited):
	# Border checks
	if x < 0 or x == N or y < 0 or y == N:
		return
	
	# Condition to check whether we can traverse via those coordinates or not
	if matrix[x][y] == 0 or visited[x][y] == True:
		return
	
	# Condition to check whether we've reached our final coordinates or not
	if x == N - 1 and y == N - 1:
		print("".join(path))
		return
	
	visited[x][y] = True 
	
	# Top Direction
	path.append("U")
	findAllWays(x - 1, y, matrix, N, path, visited)
	path.pop()
	
	# Bottom Direction
	path.append("D")
	findAllWays(x + 1, y, matrix, N, path, visited)
	path.pop()
	
	# Left Direction 
	path.append("L")
	findAllWays(x, y - 1, matrix, N, path, visited)
	path.pop()
	
	# Right Direction
	path.append("R")
	findAllWays(x, y + 1, matrix, N, path, visited)
	path.pop()
	visited[x][y]=False
	
    
path = []
visited = []
matrix = [[1, 1, 0, 0], [1, 1, 1, 1], [1, 1, 1, 0], [1, 1, 1, 1]]
n = len(matrix)

for i in range(n):
	eachRow = []
	for j in range(n):
		eachRow.append(False)
	visited.append(eachRow)
findAllWays(0, 0, matrix, n, path, visited)'''



# Initialize a string direction which represents all the directions.
direction = "DLRU"

# Arrays to represent change in rows and columns
dr = [1, 0, 0, -1]
dc = [0, -1, 1, 0]

# Function to check if cell(row, col) is inside the maze
# and unblocked


def is_valid(row, col, n, maze):
    return 0 <= row < n and 0 <= col < n and maze[row][col] == 1

# Function to get all valid paths


def find_path(row, col, maze, n, ans, current_path):
    # If we reach the bottom right cell of the matrix, add
    # the current path to ans and return
    if row == n - 1 and col == n - 1:
        ans.append(current_path)
        return
    # Mark the current cell as blocked
    maze[row][col] = 0

    for i in range(4):
        # Find the next row based on the current row (row)
        # and the dr[] array
        next_row = row + dr[i]
        # Find the next column based on the current column
        # (col) and the dc[] array
        next_col = col + dc[i]

        # Check if the next cell is valid or not
        if is_valid(next_row, next_col, n, maze):
            current_path += direction[i]
            # Recursively call the find_path function for
            # the next cell
            find_path(next_row, next_col, maze, n, ans, current_path)
            # Remove the last direction when backtracking
            current_path = current_path[:-1]

    # Mark the current cell as unblocked
    maze[row][col] = 1


# Driver code
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]

n = len(maze)
# List to store all the valid paths
result = []
# Store current path
current_path = ""

if maze[0][0] != 0 and maze[n - 1][n - 1] != 0:
    # Function call to get all valid paths
    find_path(0, 0, maze, n, result, current_path)

if not result:
    print(-1)
else:
    print(" ".join(result))