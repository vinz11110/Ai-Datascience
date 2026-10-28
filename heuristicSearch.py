import heapq

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

def a_star_search(start_state, goal_state, heuristic_function):
    """
    Function: Main puzzle solving function, running a loop until the final result is reached
    Inputs: starting state of grid, goal state of grid and which heuristic function is to be used
    Outputs: Amount of nodes tested and if goal is reached also amount of tiles moved to reach goal
    """
    #The priority queue stores tuples of: (f_score, g_score, current_state)
    queue = []
    heapq.heappush(queue, (0, 0, start_state))
    
    visited = set()
    nodes_expanded = 0  #Tracks memory usage

    while queue:
        #Extract grid state with lowest f from queue
        f_score, g_score, current_state = heapq.heappop(queue)

        #Check if goal reached
        if current_state == goal_state:
            return g_score, nodes_expanded  #Return steps taken and memory used

        #Skip already visited grid
        if current_state in visited:
            continue
            
        #Record current grid into "visited" list
        visited.add(current_state)
        nodes_expanded += 1

        #Get all valid moves by checking which numbers can be moved
        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                new_g = g_score + 1
                new_h = heuristic_function(neighbor, goal_state)
                new_f = new_g + new_h
                
                #Push the neighbor onto the priority queue
                heapq.heappush(queue, (new_f, new_g, neighbor))

    return None, nodes_expanded #If no solution is found


def heuristic_hamming(state, goal_state):
    # Calculates the Hamming distance by counting how many tiles are not in their correct position.
    # Blank tile (0) is ignored.
    # state           = current 3x3 board state
    # goal_state      = target 3x3 board state
    # misplaced_count = total number of misplaced tiles

    misplaced_count = 0
    for i in range(len(state)):
        if state[i] != 0 and state[i] != goal_state[i]:
            misplaced_count += 1

    return misplaced_count

def heuristic_manhatten(state, goal_state):
    # Calculates the Manhatten distance by summing vertical and horizontal distances of each tile to its
    # target position. Blank tile (0) is ignored.
    # state          = current 3x3 board state
    # goal_state     = target 3x3 board state
    # total_distance = sum of all Manhatten distances

    total_distance = 0
    for i in range(len(state)):
        tile = state[i]

        if tile != 0:
            # Find index of the current tile in the goal state
            goal_index = goal_state.index(tile)

            # Calculating current coordinates
            current_row = i // 3
            current_col = i % 3

            # Calculating goal coordinates
            goal_row = goal_index // 3
            goal_col = goal_index % 3

            # Adding the absolute distance to the total
            total_distance += abs(current_row - goal_row) + abs(current_col - goal_col)

    return total_distance
