from .shared import read_input
import time 


def solve_part1(data:list[str]) -> int:
    start = 50
    password = 0

    for line in data:
        # print(f"Processing line: {line}")
        direction = line[0]
        value = int(line[1:])
        step = start + value if direction == 'R' else start - value
        # print(f"Start: {start}, Direction: {direction}, Value: {value}")
        # print(f"Step calculated: {step}")
        if step == 0 or (step % 100) == 0:
            password += 1
        
        # print(f"Updated password: {password}")
        start = step

    return password


def solve_part2(data:list[str]) -> int:
    pass


if __name__ == "__main__":

    day_number = 1
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
    
