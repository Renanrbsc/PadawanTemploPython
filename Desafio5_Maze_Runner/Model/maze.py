import random


class Maze:
    def __init__(self):
        self.base_maze = []
        self.letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        self.walls = []

    def create_base_maze(self) -> list:
        for index_row in self.letter:
            unidimension = []
            for index in range(10):
                position = index_row + self.letter[index]
                unidimension.append({'pos': position, 'Space': 0, 'Used': 0})
            self.base_maze.append(unidimension)
        return self.base_maze

    def generate_walls_in_the_maze(self):
        for row in self.base_maze:
            if row is self.base_maze[0] or row is self.base_maze[-1]:
                for column in row:
                    column['Space'] = 1
                    self.walls.append(column['pos'])
            for column in row:
                if column is row[0] or column is row[-1]:
                    column['Space'] = 1
                    self.walls.append(column['pos'])
        return self.base_maze

    def generate_way(self):
        list_positions = []

        start_position = random.choice(self.walls)
        list_positions.append(start_position)

        print(list_positions)
        number_letter_in_list = len(self.letter)
        for i in range(20):
            two_letter = []
            four_letter = []
            for index, value in enumerate(list_positions[-1]):
                two_letter.append([index, value])

            position = two_letter[0][1] + two_letter[1][1]
            for row in self.base_maze:
                for column in row:
                    if position == column['pos']:
                        if column['Used'] == 0:
                            column['Used'] = 2

            print(two_letter)

            # randomiza coluna ou linha
            new_letter = random.choice(two_letter)

            # posiçao da letra na lista de letras
            index_letter = self.letter.index(new_letter[1])

            # nova letra da lista de letras
            new_position = random.choice([index_letter + 1, index_letter - 1])

            # # verifica se a letra não é a mesma da posição
            # if new_letter_position in list_positions[-1][0]:

            new_letter_position = ''
            if 0 < new_position < number_letter_in_list:
                new_letter_position += self.letter[new_position]
            elif new_position < 0:
                new_letter_position += self.letter[new_position + 2]
            elif new_position > number_letter_in_list:
                new_letter_position += self.letter[new_position - 2]
            else:
                new_letter_position += new_letter[1]

            if new_letter[0] == 0:
                position = new_letter_position + two_letter[1][1]
            else:
                position = two_letter[0][1] + new_letter_position

            list_positions.append(position)

        print(list_positions)


a = Maze()
b = a.create_base_maze()

c = a.generate_walls_in_the_maze()
a.generate_way()
for i in c:
    string = ''
    for j in i:
        string += f"{str(j['Used'])} "
    print(string)

for i in c:
    string = ''
    for j in i:
        string += f"{j['pos']} "
    print(string)
