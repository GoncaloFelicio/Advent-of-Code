from itertools import zip_longest
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

    # Transpose the matrix
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            # Take the element from the original row 'r' at column 'c'
            new_row.append(matrix[r][c])
        transposed.append(new_row)
    # print(f"Transposed: {transposed}")

    # Can make this into a function
    # Iterate through the signal length and perform operations on the corresponding column
    curr_sum = 0
    for i in range(0, len(operators)):
        # print(f"Processing signal at index {i}: {operators[i]}")
        # print (f"Corresponding column: {transposed[i]}")
        if operators[i] == '*':
            # multiply all the values in col i
            result = 1
            for val in transposed[i]:
                result *= val
            # print(f"Result of multiplication: {result}")
        elif operators[i] == '+':
            result = sum(transposed[i])
            # print(f"Result of addition: {result}")
        curr_sum += result
        # print(f"Current sum: {curr_sum}")
    
    return curr_sum


def solve_part2(data:list[str]) -> int:
    # the trick for part 2 is to keep the whitespaces in the input so that empty entries are preserved when transposing

    # The last line contains the multiplication or addition signal
    signal = data[-1]
    values = data[:-1]
    # print(f"Values: {values}")
    operators = [char for char in signal.split()]
    # print(f"Operators: {operators}")
    # Zip is the same as the transpose function above
    cepha_read= list(zip(*values))
    # print(f"Cepha Ops: {cepha_read}")
    cepha_items = ["".join(item).strip() for item in cepha_read]
    # print(f"Cepha Items: {cepha_items}")
    cepha = []
    cepha_column = []
    for item in cepha_items:
        if item:
            cepha_column.append(int(item))
        else:
            cepha.append(cepha_column)
            cepha_column = []
    # print(f"Cepha Columns: {cepha}")
    curr_sum = 0
    for i in range(0, len(operators)):
        # print(f"Processing signal at index {i}: {operators[i]}")
        # print (f"Corresponding column: {cepha[i]}")
        if operators[i] == '*':
            # multiply all the values in col i
            result = 1
            for val in cepha[i]:
                result *= val
            # print(f"Result of multiplication: {result}")

        elif operators[i] == '+':
            result = sum(cepha[i])
            # print(f"Result of addition: {result}")
        
        curr_sum += result
        # print(f"Current sum: {curr_sum}")
    
    return curr_sum


if __name__ == "__main__":
    # Execute with: python3 -m src.day06

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
        print("Solution complexity (P1): ")

        start_p2 = time.perf_counter()
        result_p2 = solve_part2(input_data)
        end_p2 = time.perf_counter()
        print(f"Day {day_number} - Part 2 Result: {result_p2} (Time: {end_p2 - start_p2:.6f} seconds)")

    else:
        print("\n--- Input Read FAILED ---")
        print("Please check if the 'data/day01_input.txt' file exists.")
    
