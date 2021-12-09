# day9-part1.py

def check_lowpoint(heightmap, row, col):
    # if row != 0:
    #     print(f' {heightmap[row-1][col]} ')
    # if col != 0 and col != len(heightmap[row])-1:
    #     print(f'{heightmap[row][col-1]}{heightmap[row][col]}{heightmap[row][col+1]}')
    # elif col == 0:
    #     print(f' {heightmap[row][col]}{heightmap[row][col+1]}')
    # else:
    #     print(f'{heightmap[row][col-1]}{heightmap[row][col]} ')
    # if row != len(heightmap)-1:
    #     print(f' {heightmap[row+1][col]} ')
    
    if row != 0 and heightmap[row][col] >= heightmap[row-1][col]:
        return False
    
    if col != 0 and heightmap[row][col] >= heightmap[row][col-1]:
        return False
    
    if col != len(heightmap[row])-1 and heightmap[row][col] >= heightmap[row][col+1]:
        return False

    if row != len(heightmap)-1 and heightmap[row][col] >= heightmap[row+1][col]:
        return False

    return True

heightmap = list()
with open('test-input.txt', 'r') as file:
    for row in file:
        row = row.rstrip()
        # print(row)
        heightmap.append([int(value) for value in row])
# print(heightmap)

list_of_lowpoints = list()
values_of_lowpoints = list()

for row in range(len(heightmap)):
    for col in range(len(heightmap[row])):
        # print(f'{heightmap[row][col]} ({row},{col}): {check_lowpoint(heightmap, row, col)})')
        if check_lowpoint(heightmap, row, col):
            list_of_lowpoints.append((row, col))
            values_of_lowpoints.append(heightmap[row][col])
print(f'Number of lowpoints: {len(list_of_lowpoints)} {list_of_lowpoints}')
print(f'Values of lowpoints: {values_of_lowpoints}')

risk_levels_of_lowpoints = list()
for value in values_of_lowpoints:
    risk_levels_of_lowpoints.append(value+1)

print(f'Risk levels of lowpoints: {risk_levels_of_lowpoints}')
print(f'Sum of risk level: {sum(risk_levels_of_lowpoints)}')