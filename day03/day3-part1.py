# day3-part1.py

with open('input.txt', 'r') as file:
    file_content = file.read()

rows = file_content.split('\n')
# print(rows)

bits = dict()
for col in range(len(rows[0])):
    bits[str(col)] = dict()
    for row in rows:
        bits[str(col)][row[col]] = bits[str(col)].get(row[col], 0) + 1

gamma_string = ''
for _, value in bits.items():
    max_count = 0
    bit_to_add = ''
    for bit, count in value.items():
        if count > max_count:
            bit_to_add = bit
            max_count = count
        
    gamma_string += bit_to_add

gamma_rate = int(gamma_string, 2)
print(gamma_string, gamma_rate)

epsilon_string = gamma_string.replace('1', '2').replace('0', '1').replace('2', '0')
epsilon_rate = int(epsilon_string, 2)
print(epsilon_string, epsilon_rate)

print(gamma_rate * epsilon_rate)
