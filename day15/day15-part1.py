# day15-part1.py

with open('test-input.txt', 'r') as file:
    file_contents = file.read()

rows = file_contents.split('\n')

def next_step(matrix, steps_taken, current_step, previous_step=None):
    if not previous_step:
        previous_step = current_step
    c_row, c_col = current_step
    p_row, p_col = previous_step
    max_row = len(matrix)
    max_col = len(matrix[c_row])
    if c_row == max_row and c_col == max_col:
        return None

    steps_taken += current_step

    d_row = p_row - c_row
    d_col = p_col - c_col

    # Down
    if c_row != max_row-1 and d_row != 1:
        direction = 'down'
        n_row = c_row + 1
        n_col = c_col
        print(f'Going {direction} from {current_step} to ({n_row}, {n_col}).')
        next_step(matrix, (c_row, c_col), (n_row, n_col))
    # Right
    if c_col != max_col-1 and d_col != 1:
        direction = 'right'
        n_row = c_row
        n_col = c_col + 1
        print(f'Going {direction} from {current_step} to ({n_row}, {n_col}).')
        next_step(matrix, (c_row, c_col), (n_row, n_col))
    # Up
    # if c_row != 0 and d_row != -1:
    #     direction = 'up'
    #     n_row = c_row - 1
    #     n_col = c_col
    #     print(f'Going {direction} from {current_step} to ({n_row}, {n_col}).')
    #     # next_step(matrix, (c_row, c_col), (n_row, n_col))
    # # Left
    # if c_col != 0 and d_col != -1:
    #     direction = 'left'
    #     n_row = c_row
    #     n_col = c_col - 1
    #     print(f'Going {direction} from {current_step} to ({n_row}, {n_col}).')
    #     # next_step(matrix, (c_row, c_col), (n_row, n_col))

    return steps_taken
    

matrix = list()

for row in rows:
    matrix += [[int(value) for value in row]]

steps_taken = list()
# next_step(matrix, steps_taken, (0, 0))

next_steps = dict()
max_row = len(matrix)
max_col = len(matrix[0])
for row in range(max_row):
    for col in range(max_col):
        next_steps[(row, col)] = list()

        if row != 0:
            next_steps[(row, col)] += [(row-1, col)]
        if row != max_row-1:
            next_steps[(row, col)] += [(row+1, col)]
        if col != 0:
            next_steps[(row, col)] += [(row, col-1)]
        if col != max_col-1:
            next_steps[(row, col)] += [(row, col+1)]
        print(f'({row}, {col}): {next_steps[(row, col)]}')

