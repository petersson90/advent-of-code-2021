# day13-part1.py

with open('input.txt', 'r') as file:
    file_contents = file.read()

rows = file_contents.split('\n')

def draw_dots(dots):
    max_x = 0
    max_y = 0
    for x, y in dots:
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

    drawing = list()
    for y in range(max_y+1):
        drawing.append(list())
        # print(f'{y:3}. ', end='')
        for x in range(max_x+1):
            drawing[y].append('-')

            if (x, y) in dots:
                drawing[y][x] = '#'
            # print(drawing[y][x], end='')
        # print()

dots = list()
fold_instructions = list()
for row in rows:
    if row == '':
        continue
    elif row.startswith('fold'):
        instruction = row.split()[2]
        fold_instructions.append(instruction)
    else:
        x, y = row.split(',')
        dots.append((int(x), int(y)))

draw_dots(dots)

for instruction in fold_instructions:
    axis, line = instruction.split('=')
    line = int(line)
    new_dots = list()
    if axis == 'y':
        print(f'Folding by line {line}')
        for dot in dots:
            # print(f'{dot} ', end='')
            y = dot[1]
            if y > line:
                # print(f'will be moved')
                x = dot[0]
                new_y = y - ((y - line) * 2)
                if (x, new_y) not in new_dots:
                    new_dots.append((x, new_y))
            else:
                new_dots.append(dot)
                # print()
    elif axis == 'x':
        print(f'Folding by column {line}')
        for dot in dots:
            x = dot[0]
            if x > line:
                y = dot[1]
                new_x = x - ((x - line) * 2)
                if (new_x, y) not in new_dots:
                    new_dots.append((new_x, y))
            else:
                if dot not in new_dots:
                    new_dots.append(dot)
    dots = new_dots
    draw_dots(dots)
    print(len(dots))
