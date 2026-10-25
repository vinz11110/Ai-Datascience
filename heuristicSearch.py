goal_state = (0, 1, 2, 3, 4, 5, 6, 7, 8)

def row_calc(index):
    """
    Function: Calculates the row within the 3x3 grid
    Inputs: Array index for a number on the grid
    Outputs: row number
    """
    row = index // 3
    return row

def col_calc(index):
    """
    Function: Calculates the column within the 3x3 grid
    Inputs: Array index for a number on the grid
    Outputs: column number
    """
    col = index % 3
    return col

def get_neighbors(state):
    """
    Function: Generates all valid next states by sliding the blank tile.
    Inputs: state (tuple representing the 3x3 board)
    Outputs: list of tuples (all valid adjacent states)
    """
    neighbors = []
    z_idx = state.index(0)  #Find the blank space
    row = row_calc(z_idx)
    col = col_calc(z_idx)

    # Define valid index movements (Up, Down, Left, Right)
    possible_moves = []
    if row > 0: possible_moves.append(z_idx - 3) #Move Up
    if row < 2: possible_moves.append(z_idx + 3) #Move Down
    if col > 0: possible_moves.append(z_idx - 1) #Move Left
    if col < 2: possible_moves.append(z_idx + 1) #Move Right

    for move_idx in possible_moves:
        #Convert tuple to list to allow swapping
        new_state = list(state)
        #Swap the 0 with the target tile
        new_state[z_idx], new_state[move_idx] = new_state[move_idx], new_state[z_idx]
        #Convert back to tuple and add to results
        neighbors.append(tuple(new_state))

    return neighbors

def checkSolvability(start_state):
    """
    Function: Calculates solvability of the starting grid using inversion count
    Inputs: starting state of grid
    Outputs: boolean based on calculation
    """
    # Remove the blank tile (0) for the math to work
    flat_state = [tile for tile in state if tile != 0]
    inversions = 0
    
    # Compare every tile to all the tiles that come after it
    for i in range(len(flat_state)):
        for j in range(i + 1, len(flat_state)):
            if flat_state[i] > flat_state[j]:
                inversions += 1
                
    return inversions % 2 == 0