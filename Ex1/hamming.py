start_state = (7, 2, 4, 5, 0, 6, 8, 3, 1)
goal_state = (0, 1, 2, 3, 4, 5, 6, 7, 8)
current_array

def hamming_distance(current_state):
    misplaced = 0
    for i in range(len(current_state)):
        tile = current_state[i]
        if tile != 0 and tile != goal_state[i]:
            misplaced += 1
    return misplaced
def row_calc(x):
    row = x // 3
    return row
def col_calc(x):
    col = x % 3
    return col
def array_values(array):
    col_array = ()
    row_arry= ()
    for i in range(len(current_state)):
        col_array += (col_calc(current_state[i]),)
        row_arry += (row_calc(current_state[i]),)
    return (col_array, row_arry)
def z_neighbours(current_state):
    results=()
    z_col = col_calc(current_state.index(0))
    z_row = row_calc(current_state.index(0))
    col_array, row_array = array_values(current_state)
    for i in range(len(current_state)):
        if z_col == col_array[current_state.index(i)] and z_row-1 == row_array[current_state.index(i)] or z_col == col_array[current_state.index(i)] and z_row+1 == row_array[current_state.index(i)] or z_row == row_array[current_state.index(i)] and z_col-1 == col_array[current_state.index(i)] or z_row == row_array[current_state.index(i)] and z_col+1 == col_array[current_state.index(i)]:
            results += (current_state[i],)
    return results
def test_neighbours(current_state):
    results = ()
    neighbours = z_neighbours(current_state)
    z_pos = current_state.index(0)
    for i in range(len(neighbours)):
        test_state = current_state
        test_state[neighbours[i]] = z_pos
        test_state[z_pos] = neighbours[i]
        results += (hamming_distance(test_state),)
    return min(results)
