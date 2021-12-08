# main.py

class Submarine():
    def __init__(self):
        self.horizontal = 0
        self.depth = 0

    def movement(self, move, distance):
        if move == 'forward':
            self.horizontal += distance
        elif move == 'down':
            self.depth += distance
        elif move == 'up':
            self.depth -= distance

        return self.horizontal, self.depth

if __name__ == "__main__":
    submarine = Submarine()
    with open("input.txt", "r") as file:
        for row in file:
            row = row.rstrip()

            row_data = row.split(" ")
            move = row_data[0]
            distance = int(row_data[1])

            submarine.movement(move, distance)

    print(submarine.horizontal, '*', submarine.depth, '=', submarine.horizontal * submarine.depth)