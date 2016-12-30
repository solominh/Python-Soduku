import test_generator
import test_generator2
from sudoku_solver import SudkuSolver, print_result


test = test_generator2.generate_test()
print_result(test)

result = SudkuSolver().get_one_solution(test)
print_result(result)

new_test = test_generator.generate_puzzle_from(result)
print_result(new_test)



