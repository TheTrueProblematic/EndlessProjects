
# Hi delightful programmers out there! Today, we're going to solve some glorious KenKen puzzles!
# You might be wondering, "What the heck is KenKen?" Well, it's a math-based logic puzzle
# All we need is Python's magic! So buckle up, and let's solve some puzzles!

def print_grid(grid):
    """
    This function prints the puzzle for us which we'll be solving, not really necessary 
    but nice to know what we're up against.
    """
    for i in range(6):
        for j in range(6):
            print(grid[i][j], end = ' ')
        print()

def is_valid(grid, row, col, num):
    """
    This checks if a number can be placed at the grid[row][col] according to KenKen rules
    """
    # First check the row
    for x in range(6):
        if grid[row][x] == num:
            return False

    # Then check the column
    for x in range(6):
        if grid[x][col] == num:
            return False

    # This finds the top left corner of the cage and checks if the number exists in the cage
    startRow = row - row % 2
    startCol = col - col % 3
    for i in range(2):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
                
    # Everything seems okay to me, you can proceed!
    return True

def kenken_solver(grid, row=0, col=0):
    """
    This function, my friend, is our main puzzle solver. 
    It will use the 'good old' backtracking method to fill the grid 
    with correct numbers according to KenKen rules.
    """
    # Check if we have reached the end
    if (row == 6 - 1 and col == 6): 
        return True

    # Check if column value  becomes more than 6, and we move to next row and column start from 0
    if col == 6: 
        row += 1
        col = 0

    # Check if this cell is already filled
    if grid[row][col] > 0:
        return kenken_solver(grid, row, col + 1)

    for num in range(1, 7):

        # Check if it is possible to place this num here
        if is_valid(grid, row, col, num):  
            grid[row][col] = num

            # Recursively check if this placement can lead us to a solution
            if kenken_solver(grid, row, col + 1): 
                return True

        # If not possible to place the number there, reset the cell value
        grid[row][col] = 0

    # If all the numbers have been checked and no number can be placed here, return False
    return False
    
# Starting grid with 0 as empty cells 
grid = [[0 for x in range(6)]for y in range(6)] 

# Let's call our glorious solver
print("Let's solve this KenKen puzzle! Here we go!")
if (kenken_solver(grid)== False):
    print ("Solution doesn't exist, Maybe you're in a parallel universe.")
else:
    print ("The solved KenKen puzzle is:")
    print_grid(grid)
