# day11-part1.py

with open('input.txt', 'r') as file:
    file_contents = file.read()

rows = file_contents.split('\n')

octopuses = dict()
for row_no, row in enumerate(rows):
    for col_no, value in enumerate(row):
        octopuses[(row_no, col_no)] = int(value)

max_row = len(rows) - 1 # Minus one to cater for 0 based counting
max_col = len(rows[0]) - 1 # Minus one to cater for 0 based counting

def run_step(octopuses):
    for key in octopuses:
        increase_one(octopuses, key)
    
    flashed = list()
    for key in octopuses:
        if octopuses[key] > 9:
            flashing_octopus(octopuses, key, flashed)

    for key in flashed:
        octopuses[key] = 0

    print(f'{len(flashed)}: {flashed}')

    return len(flashed)

    # print(flashed)

def increase_one(octopuses, key):
    # print(f'{key} increased from {octopuses[key]} to {octopuses[key] + 1}')
    octopuses[key] += 1

def check_matrix(octopuses, flashed):
    for key in octopuses:
        if octopuses[key] > 9:
            # print(f'{key} has value {octopuses[key]}')
            flashing_octopus(octopuses, key, flashed)


def flashing_octopus(octopuses, key, flashed):
    if key in flashed:
        return None
    
    flashed.append(key)
    # print(f'{key} flashing')

    row, col = key

    if row != 0 and col != 0: # Diagonal top-left
        increase_one(octopuses, (row-1, col-1))
    if row != 0: # Above
        increase_one(octopuses, (row-1, col))
    if row != 0 and col != max_col: # Diagonal top-right
        increase_one(octopuses, (row-1, col+1))
    if col != 0: # Left
        increase_one(octopuses, (row, col-1))
    if col != max_col: # Right
        increase_one(octopuses, (row, col+1))
    if row != max_row and col != 0: # Diagonal bottom-left
        increase_one(octopuses, (row+1, col-1))
    if row != max_row: # Below
        increase_one(octopuses, (row+1, col))
    if row != max_row and col != max_col: # Diagonal bottom-right
        increase_one(octopuses, (row+1, col+1))

    check_matrix(octopuses, flashed)


total_flashes = 0
print(f'--- Step 0 ---')
# for row_no in range(len(rows)):
#     print([octopuses[(row_no, col_no)] for col_no in range(len(rows[0]))])

for iteration in range(100):
    print(f'--- Step {iteration + 1} ---')
    total_flashes += run_step(octopuses)
    # for row_no in range(len(rows)):
    #     print([octopuses[(row_no, col_no)] for col_no in range(len(rows[0]))])

print(f'After step {iteration + 1}, there has been {total_flashes} flashes')