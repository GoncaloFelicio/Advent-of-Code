from .shared import read_input
import time 

def solve_part1(data:list[str]) -> int:
    
    def get_max(iterable: list[str]) -> tuple[int, str]:
        # Set the first item as the initial maximum value
        current_idx = 0
        current_max = None

        # enumerate already calls iter() and next() internally
        for idx, item in enumerate(iterable):
            if idx == 0:
                current_max = item
                continue

            if item > current_max:
                current_max = item
                current_idx = idx

        return (current_idx, current_max)
    
    result = 0
    for line in data:
        # get the first max value and its index
        max_idx, max_value = get_max(line)
        # print(f"Max value in line '{line}': {max_value}, at index '{max_idx}' -> {line[max_idx]}")
        
        # if idx is last, get the second max value and its index by looking backward
        if max_idx == len(line) - 1:
            adj_line = line[:max_idx]
            second_max_idx, second_max_value = get_max(adj_line)
            adj_second_max_idx = second_max_idx
            # print(f"Second Max value in line '{adj_line}': {second_max_value}, at index '{adj_second_max_idx}' -> {line[adj_second_max_idx]}")
        
        # get the second max value and its index by looking forward from the first max index
        else:
            adj_line = line[max_idx + 1:]
            second_max_idx, second_max_value = get_max(adj_line)
            adj_second_max_idx = second_max_idx + max_idx + 1
            # print(f"Second Max value in line '{adj_line}': {second_max_value}, at index '{adj_second_max_idx}' -> {line[adj_second_max_idx]}")

        # calculate largest joltage based on index positions
        largest_joltage = int(max_value + second_max_value) if max_idx < adj_second_max_idx else int(second_max_value + max_value)
        # print(f"Largest Joltage from line '{line}': {largest_joltage}")
        result += largest_joltage

    # print(f"Final Result: {result}")
    return result

def solve_part2(data:list[str]) -> int:
    pass


if __name__ == "__main__":

    day_number = 3
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
        print("Solution complexity (P1): O(n)")

        start_p2 = time.perf_counter()
        result_p2 = solve_part2(input_data)
        end_p2 = time.perf_counter()
        print(f"Day {day_number} - Part 2 Result: {result_p2} (Time: {end_p2 - start_p2:.6f} seconds)")
        print(f"Execution Time (P2): {end_p2 - start_p2:.6f} seconds")

    else:
        print("\n--- Input Read FAILED ---")
        print("Please check if the 'data/day01_input.txt' file exists.")
    
