from .shared import read_input
import time 

def solve_part1(data:list[str]) -> int:
    
    result = 0
    for _range in data[:11]:
        range_min, range_max = _range.split('-')
        start_digits = len(range_min)
        # print(f"Range Min: {range_min}, Range Max: {range_max}")
        Hstart_digits = start_digits / 2 if start_digits % 2 == 0 else (start_digits // 2) + 1
        # print(f"Start Digits: {start_digits}, Half Start Digits: {Hstart_digits}")
        end_digits = len(range_max)
        Hend_digits = end_digits / 2 if end_digits % 2 == 0 else (end_digits // 2) + 1
        # print(f"End Digits: {end_digits}, Half End Digits: {Hend_digits}")
        Hstart = int(range_min[:int(Hstart_digits)])
        Hend = int(range_max[:int(Hend_digits)])
        # print(f"Half Start: {Hstart}, Half End: {Hend}")

        if Hstart > Hend:
            Hstart = int(range_min[:int(Hstart_digits) - 1])
            # print(f"Adjusted Half Start: {Hstart}")
        
        # print(f"Range: {_range}, Half Start: {Hstart}, Half End: {Hend}")

        # Calculte palindromic numbers in the range and cumulate the sum if valid
        for H in range(Hstart, Hend + 1):
            H = H + H * 10 ** len(str(H))
            # print(f"Palindromic Number: {H}")

            if H >= int(range_min) and H <= int(range_max):
                print(f"Valid Palindromic Number in Range: {H}")
                result += H

    return result
def solve_part2(data:list[str]) -> int:
    
    
    pass

if __name__ == "__main__":

    day_number = 2
    input_data = read_input(day_number)

    if input_data:
        print(f"Input data for day {day_number}, First 10 lines:")
        for line in input_data[:10]:
            print(line)
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
    
