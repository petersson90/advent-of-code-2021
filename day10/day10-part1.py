# day10-part1.py

with open('test-input.txt', 'r') as file:
    file_contents = file.read()

rows = file_contents.split('\n')

chunk_characters = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

rows_to_check = list()
for row in rows:
    open_chunks = list()
    for character in row:
        expected_ending = ''
        if len(open_chunks) > 0:
            expected_ending = chunk_characters.get(open_chunks[-1])

        if character in chunk_characters:
            open_chunks.append(character)
        elif character == expected_ending:
            open_chunks.pop(-1)
        else:
            print(open_chunks)
            print(f'Expected {expected_ending}, but found {character} instead.')
            rows_to_check.append(row)
            break
    
    # print(open_chunks)
print(rows_to_check)
