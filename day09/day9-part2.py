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

def basin_size(heightmap, row, col, basin_coordinates=list(), checked_coordinates=list()):
    if (row, col) in basin_coordinates or (row, col) in checked_coordinates:
        return None
    
    checked_coordinates.append((row, col))
    basin_coordinates.append((row, col))
    # print(basin_coordinates, checked_coordinates)

    if row != 0 and heightmap[row][col] < heightmap[row-1][col] and heightmap[row-1][col] != 9:
        basin_size(heightmap, row-1, col, basin_coordinates, checked_coordinates)
    if col != 0 and heightmap[row][col] < heightmap[row][col-1] and heightmap[row][col-1] != 9:
        basin_size(heightmap, row, col-1, basin_coordinates, checked_coordinates)
    if col != len(heightmap[row])-1 and heightmap[row][col] < heightmap[row][col+1] and heightmap[row][col+1] != 9:
        basin_size(heightmap, row, col+1, basin_coordinates, checked_coordinates)
    if row != len(heightmap)-1 and heightmap[row][col] < heightmap[row+1][col] and heightmap[row+1][col] != 9:
        basin_size(heightmap, row+1, col, basin_coordinates, checked_coordinates)

    return checked_coordinates, basin_coordinates

heightmap = list()
with open('input.txt', 'r') as file:
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

basins = dict()
for row, col in list_of_lowpoints:
    basins[(row, col)] = list()
    basin_size(heightmap, row, col, basins[(row, col)])

# print(basins)
top_three = list()
for basin, list_of_coordinates in basins.items():
    size_of_basin = len(list_of_coordinates)
    print(basin, size_of_basin)

    top_three.sort()

    if len(top_three) < 3:
        top_three.append(size_of_basin)
    elif size_of_basin > top_three[0]:
        top_three[0] = size_of_basin

sum_of_top_three = 1
for value in top_three:
    sum_of_top_three *= value
print(f'{top_three} = {sum_of_top_three}')