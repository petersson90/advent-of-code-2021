# day3-part1.py

with open('input.txt', 'r') as file:
    file_content = file.read()

rows = file_content.split('\n')
# print(rows)

def frequency(input_list, if_draw='1'):
    counts = dict()
    for character in input_list:
        counts[character] = counts.get(character, 0) + 1
    
    selected_character = ''
    count = -1
    for key, value in counts.items():
        if count == -1 or (value > count and if_draw == '1') or (value < count and if_draw == '0') or (value == count and key == if_draw):
            selected_character = key
            count = value
    
    return selected_character

oxygen_rating_rows = rows.copy()
bit_string = ''
for pos in range(len(oxygen_rating_rows[0])):
    bit = frequency([row[pos] for row in oxygen_rating_rows], '1')
    bit_string += bit
    # print(f'--- position {pos}: {bit_string} ---')
    oxygen_rating_rows = [row for row in oxygen_rating_rows if row[pos] == bit]
    # print(oxygen_rating_rows)

    if len(oxygen_rating_rows) == 1:
        break

co2_scrubber_rows = rows.copy()
bit_string = ''
for pos in range(len(co2_scrubber_rows[0])):
    bit = frequency([row[pos] for row in co2_scrubber_rows], '0')
    bit_string += bit
    # print(f'--- position {pos}: {bit_string} ---')
    co2_scrubber_rows = [row for row in co2_scrubber_rows if row[pos] == bit]
    # print(co2_scrubber_rows)

    if len(co2_scrubber_rows) == 1:
        break


print(f'{oxygen_rating_rows[0]} = {int(oxygen_rating_rows[0], 2)}')
print(f'{co2_scrubber_rows[0]} = {int(co2_scrubber_rows[0], 2)}')
print(f'Life support rating = {int(oxygen_rating_rows[0], 2) * int(co2_scrubber_rows[0], 2)}')