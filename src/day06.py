import signal
from .shared import read_input
import time 


def solve_part1(data:list[str]) -> int:
    
    # The last line contains the multiplication or addition signal
    signal = data[-1]
    # print(f"Signal: {signal}")
    values = data[:-1]
    # print(f"Values: {values}")

    operators = [char for char in signal.split()]
    # print(f"Operators: {operators}")

    # Clean string to matrix of ints
    matrix = []
    for row in values:
        # change string to list of ints
        int_values = [int(char) for char in row.split()]
        # print(int_values)
        matrix.append(int_values)
    # print(f"Matrix: {matrix}")


    # transpose the matrix
    # Get dimensions
    rows = len(matrix)
    cols = len(matrix[0])

    # 1. Create an empty grid for the result (Cols x Rows)
    transposed = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            # Take the element from the original row 'r' at column 'c'
            new_row.append(matrix[r][c])
        transposed.append(new_row)
    # print(f"Transposed: {transposed}")

    # Iterate through the signal and perform operations on the corresponding column
    curr_sum = 0
    for i in range(0, len(operators)):
        # print(f"Processing signal at index {i}: {operators[i]}")
        # print (f"Corresponding column: {transposed_m[i]}")
        if operators[i] == '*':
            # multiply all the values in col i
            col_values = transposed[i]
            # print(f"Col values to multiply: {col_values}")
            result = 1
            for val in col_values:
                result *= val
            # print(f"Result of multiplication: {result}")

        elif operators[i] == '+':
            # add all the values in col i
            col_values = transposed[i]
            # print(f"Col values to add: {col_values}")
            result = sum(col_values)
            # print(f"Result of addition: {result}")
        
        curr_sum += result
        # print(f"Current sum: {curr_sum}")
    return curr_sum


def solve_part2(data:list[str]) -> int:

    pass


if __name__ == "__main__":

    day_number = 6
    input_data = read_input(day_number)

    if input_data:
        # print(f"Input data for day {day_number}, First 10 lines:")
        # for line in input_data[:10]:
        #     print(line)
        start_p1 = time.perf_counter()
        result_p1 = solve_part1(input_data)
        end_p1 = time.perf_counter()
        print(f"Day {day_number} - Part 1 Result: {result_p1} (Time: {end_p1 - start_p1:.6f} seconds)")
        print(f"Execution Time (P1): {end_p1 - start_p1:.6f} seconds")
        print("Solution complexity (P1): ")

        start_p2 = time.perf_counter()
        result_p2 = solve_part2(input_data)
        end_p2 = time.perf_counter()
        print(f"Day {day_number} - Part 2 Result: {result_p2} (Time: {end_p2 - start_p2:.6f} seconds)")
        print(f"Execution Time (P2): {end_p2 - start_p2:.6f} seconds")

    else:
        print("\n--- Input Read FAILED ---")
        print("Please check if the 'data/day01_input.txt' file exists.")
    
