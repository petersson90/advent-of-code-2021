# day14-part1.py

with open('input.txt', 'r') as file:
    file_contents = file.read()

rows = file_contents.split('\n')

base_string = rows[0]

pair_to_char = dict()
for row in rows[2:]:
    pair, _, char_to_insert = row.split()
    pair_to_char[pair] = char_to_insert
# print(pair_to_char)

def string_iteration(input_string):
    # print(input_string)
    string_pairs = list()
    for char_no in range(len(input_string)-1):
        string_pairs.append(input_string[char_no:char_no+2])

    new_string = ''
    for pair in string_pairs:
        insert = pair_to_char.get(pair)
        new_pair = pair[0] + insert + pair[1]
        # print(f'{pair} -> {new_pair}', end=': ')
        if new_string == '':
            new_string += new_pair
        else:
            new_string += new_pair[1:]
        # print(new_string)
    return new_string

def count_characters(input_string):
    characters = dict()
    for character in input_string:
        characters[character] = characters.get(character, 0) + 1
    
    # most_common = ''
    max_value = None
    # least_common = ''
    min_value = None
    for key, value in characters.items():
        if max_value is None or value > max_value:
            max_value = value
            # most_common = key
        if min_value is None or value < min_value:
            min_value = value
            # least_common = key
    
    return characters, max_value - min_value

print(f'Template: {base_string}')
for i in range(10):
    base_string = string_iteration(base_string)
    # print(f'After step {i+1}: {base_string}')

print(count_characters(base_string))