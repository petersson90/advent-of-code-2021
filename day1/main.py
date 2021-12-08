# main.py

total_rows = 0
increases = 0
decreases = 0
same = 0
prev_value = None

def total_increases(number_list, count=1):
    prev_value = None
    increases = 0
    
    for i in range(len(number_list) - count + 1):
        curr_value = sum(number_list[i:i+count])
        if prev_value == None:
            change = 'N/A - no previous sum'
        elif curr_value == prev_value:
            change = 'no change'
        elif curr_value < prev_value:
            change = 'decreased'
        else:
            change = 'increased'
            increases += 1
        
        # print(f'{curr_value} ({change})')
        prev_value = curr_value
    
    return increases




if __name__ == "__main__":
    with open("input.txt", "r") as file:
        number_list = list()
        for row in file:
            row = row.replace("\n", "")
            number_list.append(int(row))

        print(f'Number of increases: {total_increases(number_list)}')
        print(f'Number of increases (three-at-a-time): {total_increases(number_list, 3)}')
