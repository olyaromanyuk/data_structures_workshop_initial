import copy

class Board():
    def __init__(self, size, data):
        if len(data) != size:
            raise ValueError("invalid data")
        for row in data:
            if len(row) != size:
                raise ValueError("invalid data")
        self.size = size
        self.data = copy.deepcopy(data)
        self.previous = None
        self.moves_to_reach = 0

    def _get_correct_position(self, n):
        if n == 0:
            return self.size - 1, self.size - 1
        else:
            return (n -1) // self.size , (n-1)%self.size

    def heuristic(self):
        sum = self.moves_to_reach
        for i in range(self.size):
            for j in range(self.size):
                correct_i, correct_j = self._get_correct_position(self.data[i][j])
                if self.data[i][j] != 0:
                    sum += abs(i - correct_i) + abs(j - correct_j)
        return sum

    def is_solved(self):
        return self.heuristic() == self.moves_to_reach

    def exchange_positions(self, position_1, position_2):
        twin_data = copy.deepcopy(self.data)
        tmp = twin_data[position_1[0]][ position_1[1]]
        twin_data[position_1[0]][ position_1[1]] = twin_data[position_2[0]][ position_2[1]]
        twin_data[position_2[0]][ position_2[1]] = tmp
        return Board(self.size, twin_data)

    def twin(self):
        position_1 = []
        position_2 = []
        for i in range(self.size):
            for j in range(self.size):
                if self.data[i][j] != 0:
                    if len(position_1) == 0:
                        position_1 = [i,j]
                    elif len(position_2) == 0:
                        position_2 = [i,j]
                        return self.exchange_positions(position_1,position_2)

    def neighbors(self):
        for i in range(self.size):
            try:
                index = self.data[i].index(0)
            except ValueError:
                continue
            row_0 = i
            column_0 = index

            row_moving = row_0 - 1
            if row_moving >= 0:
                b = self.exchange_positions((row_0, column_0),(row_moving,column_0))
                b.previous = self
                b.moves_to_reach = self.moves_to_reach + 1
                yield b

            row_moving = row_0 + 1
            if row_moving < self.size:
                b = self.exchange_positions((row_0, column_0), (row_moving, column_0))
                b.previous = self
                b.moves_to_reach = self.moves_to_reach + 1
                yield b

            column__moving = column_0 - 1
            if column__moving >= 0:
                b = self.exchange_positions((row_0, column_0), (row_0, column__moving))
                b.previous = self
                b.moves_to_reach = self.moves_to_reach + 1
                yield b

            column__moving = column_0 + 1
            if column__moving < self.size:
                b = self.exchange_positions((row_0, column_0), (row_0, column__moving))
                b.previous = self
                b.moves_to_reach = self.moves_to_reach + 1
                yield b


    def __repr__(self):
        return "Board:\n"+'\n'.join(['\t'.join(map(str,row)) for row in self.data ])

    def __lt__(self, other):
        return self.heuristic() < other.heuristic()
    def __gt__(self, other):
        return self.heuristic() > other.heuristic()

    def __eq__(self, other):
        return self.heuristic() == other.heuristic()


    def has_same_data(self, other):
        if self.size != other.size:
            return False
        for i in range(self.size):
            for j in range(self.size):
                if self.data[i][j] != other.data[i][j]:
                    return False
        return True



# b = Board(4,[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]])
# print(b)
#
# for neighbor in b.neighbors():
#     print(neighbor)


