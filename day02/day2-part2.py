# day2-part2.py

class Submarine():
    def __init__(self):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0

    def movement(self, move, distance):
        if move == 'forward':
            self.horizontal += distance
            self.depth += self.aim * distance
        elif move == 'down':
            self.aim += distance
        elif move == 'up':
            self.aim -= distance

        return self.horizontal, self.depth, self.aim

if __name__ == "__main__":
    submarine = Submarine()
    with open("input.txt", "r") as file:
        for row in file:
            row = row.rstrip()

            row_data = row.split(" ")
            move = row_data[0]
            distance = int(row_data[1])

            # print(row)
            submarine.movement(move, distance)

    print(submarine.horizontal, '*', submarine.depth, '=', submarine.horizontal * submarine.depth)