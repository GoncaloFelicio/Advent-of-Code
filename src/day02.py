from .shared import read_input
import time 

def solve_part1(data:list[str]) -> int:
    
    result = 0
    for _range in data[:]:
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
                # print(f"Valid Palindromic Number in Range: {H}")
                result += H

    return result


def solve_part2(data:list[str]) -> int:

    # More pythonic way and checks all combinations of repeating patterns
    def is_invalid_id(num_str: str) -> bool:
        lenght = len(num_str)
        for seg_len in range(1, lenght // 2 + 1):
            if lenght % seg_len == 0:
                repetitions = lenght // seg_len
                expected_num = num_str[:seg_len] * repetitions
                if expected_num == num_str:
                    # print(f"Invalid {seg_len}-Repeating Number Detected: {num_str}")
                    return True
        return False
    
    result = 0
    for _range in data[:]:
        range_min, range_max = _range.split('-')
        # print(f"Range Min: {range_min}, Range Max: {range_max}")
        
        for num in range(int(range_min), int(range_max) + 1):
            if is_invalid_id(str(num)):
                result += num
                # print(f"Current Result: {result}")
    return result

    # One way to do it but not very efficient and can miss >=4 digit repeating patterns
    # result = 0
    # for _range in data[:]:
    #     range_min, range_max = _range.split('-')
    #     # print(f"Range Min: {range_min}, Range Max: {range_max}")
        
    #     for num in range(int(range_min), int(range_max) + 1):
    #         num_str = str(num)
    #         # if even
    #         if len(num_str) % 2 == 0:
    #             half_len = len(num_str) // 2
    #             # check first half == second half
    #             if num_str[:half_len] == num_str[half_len:]:
    #                 # print(f"Valid Half Length Palindromic Number: {num}")
    #                 result += num
    #                 # print(f"Current Result: {result}")
    #             # check if repeats every 2 digits
    #             elif len(num_str) > 2:
    #                 length = len(num_str)
    #                 seg_len = 2
    #                 repetitions = length // seg_len
    #                 expected_num = num_str[:seg_len] * repetitions
    #                 if expected_num == num_str:
    #                     # print(f"Valid 2 Length Repeating Number: {num}")
    #                     result += num
    #                     # print(f"Current Result: {result}")
    #         # if odd
    #         else:
    #             # check for repeating single digit:
    #             if all(d == num_str[0] for d in num_str) and len(num_str) > 1:
    #                 # print(f"Valid Full Length Palindromic Number: {num}")
    #                 result += num
    #                 # print(f"Current Result: {result}")     
    #             # check if repeats every 3 digits
    #             elif len(num_str) > 3:
    #                 length = len(num_str)
    #                 seg_len = 3
    #                 repetitions = length // seg_len
    #                 expected_num = num_str[:seg_len] * repetitions
    #                 if expected_num == num_str:
    #                     # print(f"Valid 3 Length Repeating Number: {num}")
    #                     result += num
    #                     # print(f"Current Result: {result}")
    #     # print(f"Current Result: {result}")
    # return result
            

if __name__ == "__main__":

    day_number = 2
    input_data = read_input(day_number)

    if input_data:
        print(f"Input data for day {day_number}, First 3 lines:")
        for line in input_data[:3]:
            print(line)
        start_p1 = time.perf_counter()
        result_p1 = solve_part1(input_data)
        end_p1 = time.perf_counter()
        print(f"Day {day_number} - Part 1 Result: {result_p1} (Time: {end_p1 - start_p1:.6f} seconds)")
        print(f"Execution Time (P1): {end_p1 - start_p1:.6f} seconds")
        # print("Solution complexity (P1): O(n)")

        start_p2 = time.perf_counter()
        result_p2 = solve_part2(input_data)
        end_p2 = time.perf_counter()
        print(f"Day {day_number} - Part 2 Result: {result_p2} (Time: {end_p2 - start_p2:.6f} seconds)")
        print(f"Execution Time (P2): {end_p2 - start_p2:.6f} seconds")

    else:
        print("\n--- Input Read FAILED ---")
        print("Please check if the 'data/day01_input.txt' file exists.")
    
