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
def position_eval(current_state):
    results=[]
    for i in range(len(current_state)):
        if row(current_state[i])==row(current_state[current_state.index(0)]) || col(current_state[i])==col(current_state[current_state.index(0)]):
            results.append(current_state[i])
    for i in range(len(results)):
        test_state()
    return min(results)
def calc_loop(start):