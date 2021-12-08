# day1-part1.py

def total_increases(number_list):
    prev_value = None
    increases = 0
    
    for number in number_list:
        if prev_value == None:
            change = 'N/A - no previous sum'
        elif number == prev_value:
            change = 'no change'
        elif number < prev_value:
            change = 'decreased'
        else:
            change = 'increased'
            increases += 1
        
        print(f'{number} ({change})')
        prev_value = number
    
    return increases


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        number_list = list()
        for row in file:
            row = row.replace("\n", "")
            number_list.append(int(row))

        print(f'Number of increases: {total_increases(number_list)}')