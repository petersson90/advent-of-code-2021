# day5-part1.py

with open('test-input.txt', 'r') as file:
    file_contents = file.read()

rows = file_contents.split('\n')

for row in rows:
    print(row)