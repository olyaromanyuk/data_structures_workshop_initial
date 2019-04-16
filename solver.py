from board import Board
import matplotlib.pyplot as plt
from data_structures import Heap as DataStructure

import time


class Solver():
    def __init__(self, board):
        self.board = board
        self.twin_board = self.board.twin()

        self.data_structure = DataStructure()
        self.twin_data_structure = DataStructure()

        self.states_explored = -1

        current_state = self.board
        current_twin_state = self.twin_board
        while True:
            self.states_explored += 1
            # print(current_state.moves_to_reach)
            # print(current_state)
            if current_state.is_solved():
                self.solution = self._form_solution(current_state)
                break
            elif current_twin_state.is_solved():
                self.moves = -1
                self.solution = []
                break

            for neighbor in current_state.neighbors():
                if current_state.previous is None or not neighbor.has_same_data(current_state.previous):
                    self.data_structure.add(neighbor)

            for neighbor in current_twin_state.neighbors():
                if current_twin_state.previous is None or not neighbor.has_same_data(current_twin_state.previous):
                    self.twin_data_structure.add(neighbor)

            current_state = self.data_structure.get_min()
            current_twin_state = self.twin_data_structure.get_min()

    def _form_solution(self, last_state):
        solution = []
        state = last_state
        while state.previous is not None:
            solution.append(state)
            state = state.previous
        solution.append(state)
        solution.reverse()
        return solution

boards =[Board(3, [[ 1,  0,  2],[4,  6,  3],[7 , 5,  8 ]]),
         Board(3,[[ 0,  4,  1],[5,  3,  2],[7,  8,  6]]),
         Board(3,[[ 2,  0,  8],[1,  3,  5],[4,  6,  7]]),
         Board(3, [[ 7,  4, 3],[ 2,  8,  6],[0,  5,  1]]),
         Board(3,  [[6,  4,  7],[8,  5,  0],[3,  2,  1]])]


#######################################
# this board takes far too long to solve with list, save this for later
# Board(3,  [[6,  4,  7],[8,  5,  0],[3,  2,  1]])]

optimal_moves = [5,10,15,20, 31]
states_explored = []
times = []
average_time_per_step = []
for i,b in enumerate(boards):
    start = time.time()
    s = Solver(b)
    t = time.time() - start
    print("Optimal moves:\t{}\tStates explored:\t{}\tTotal time:\t{}\tTime per state explored:\t{}".format(optimal_moves[i],
                                                                                                           s.states_explored,
                                                                                                           t,
                                                                                                           t / s.states_explored))
    print()
    times.append(t)
    states_explored.append(s.states_explored)
    average_time_per_step.append(t/s.states_explored)

plt.plot(optimal_moves, times)
plt.show()
plt.plot(optimal_moves, states_explored)
plt.show()
plt.plot(optimal_moves, average_time_per_step)
plt.show()



