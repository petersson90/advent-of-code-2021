# day4-part1.py

def call_number(possible_lines, drawn_number, winning_boards):
    print(f'Calling number: {drawn_number}')
    for board, lines in possible_lines.items():
        for line in lines:
            if drawn_number in line:
                line.remove(drawn_number)
                # print(line, len(line))
            
            if len(line) == 0 and board not in winning_boards:
                winning_boards.append(board)
                print(f'Board {board} won after number {drawn_number} was drawn.')
                # print(winning_boards)
            if len(winning_boards) == len(possible_lines):
                return board

    return None


with open('input.txt', 'r') as file:
    file_contents = file.read()

rows = file_contents.split('\n\n')

called_numbers = rows[0].split(',')
# print(called_numbers)

raw_boards = rows[1:]

bingo_boards = [[number.split() for number in bingo_board.split('\n')] for bingo_board in raw_boards]

possible_lines = dict()
for board_number, board in enumerate(bingo_boards):
    possible_lines[str(board_number)] = [row for row in board]
    for col in range(len(board[0])):
        possible_lines[str(board_number)] += [[row[col] for row in board]]

winner = None
winning_boards = list()
while winner is None:
    for drawn_number in called_numbers:
        winner = call_number(possible_lines, drawn_number, winning_boards)

        if winner is not None:
            # print(f'Board {winner} won after number {drawn_number} was drawn.')
            remaining_lines = possible_lines[winner][:5]
            remaining_numbers = list()
            for line in remaining_lines:
                for number in line:
                    remaining_numbers.append(int(number))


            print(f'{sum(remaining_numbers)} * {drawn_number} = {sum(remaining_numbers) * int(drawn_number)}')
            break