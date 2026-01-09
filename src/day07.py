from itertools import zip_longest
from .shared import read_input
import time 


def solve_part1(data:list[str]) -> int:
    
    # print(data)
    rows = len(data)
    # print(f"Rows: {rows}")
    cols = len(data[0])
    # print(f"Cols: {cols}")
    start_x = -1
    for x in range(cols):
        if data[0][x] == 'S':
            start_x = x
            break
    # print(f"Start x: {start_x}, value at start: {data[0][start_x]}")
    # positions of active beams
    active_beams = {start_x}
    total_splits = 0
    # row by row except last
    for y in range(rows - 1):
        # print(f"Row {y}: {data[y]}, Active beams positions: {active_beams}")
        next_positions = set()
        splitter_hit = set()
        for x in active_beams:
            # print(f"Processing beam at position {(y, x)}")
            # if a beam is active check for a spliter int the next row
            target_pos = data[y + 1][x]
            if target_pos == '^':
                # splitter found, beam splits
                splitter_hit.add((y+1, x))
                for dx in [-1,1]:
                    new_x = x + dx
                    # print(f"Splitter at {(y+1, x)} redirects beam to {new_x}")
                    if 0 <= new_x < cols:
                        # only add new beam if within bounds
                        next_positions.add(new_x)
            else:
                # no splitter, beam continues straight
                next_positions.add(x)
        # print(f"Next positions: {next_positions}")
        # Update total splits
        total_splits += len(splitter_hit)
        # print(f"Total splits so far: {total_splits}")
        # Update active beams for next row
        active_beams = next_positions
    return total_splits
    

def solve_part2(data:list[str]) -> int:
    # Trick is to see this as a counting of unique paths the beam can take and
    # use a recursive approach with memoization
    rows = len(data)
    cols = len(data[0])
    start_x = -1
    for x in range(cols):
        if data[0][x] == 'S':
            start_x = x
            break
    
    memo = {}
    def count_paths(y:int, x:int) -> int:
        # base case: reached last row
        if y == rows - 1:
            print(f"Reached bottom at {(y, x)}")
            return 1 # reached the bottom so count this path "1", it will recursively sum up
        
        # check memoization
        print(f"Counting paths from {(y, x)}")
        # checking the key values in memo dictionary
        if (y, x) in memo:
            # Check if this path has been computed before
            print(f"Using memoized value for {(y, x)}: {memo[(y, x)]}")
            # return the stored value for this key
            return memo[(y, x)]
        
        target_pos = data[y + 1][x]
        if target_pos == '^':
            # splitter found, beam splits
            total_paths = 0
            # total paths is sum of paths from both directions
            # left path
            if x - 1 >= 0:
                # countinue to recursively count paths
                print(f"Splitter at {(y+1, x)} redirects beam left to {(y+1, x-1)}")
                total_paths += count_paths(y + 1, x - 1)
            # right path
            if x + 1 < cols:
                print(f"Splitter at {(y+1, x)} redirects beam right to {(y+1, x+1)}")
                total_paths += count_paths(y + 1, x + 1)
        else:
            # no splitter, beam continues straight
            total_paths = count_paths(y + 1, x)
            print(f"Beam at {(y, x)} continues straight to {(y+1, x)} with current paths: {total_paths}")

        # store current path in moemo
        memo[(y, x)] = total_paths
        return total_paths

    return count_paths(0, start_x)

if __name__ == "__main__":
    # Execute with: python3 -m src.day06

    day_number = 7
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
    
