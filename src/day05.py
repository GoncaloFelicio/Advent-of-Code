from .shared import read_input
import time 


def solve_part1(data:list[str]) -> int:

    # Split data at the empty line, take the first part and second part separately
    fresh_data = []
    for row in data:
        if row.strip() == "":
            break
        fresh_data.append(row)
    ingredients_data = data[len(fresh_data) + 1:]

    # check if ingredients number are within any of the ranges
    valid_count = 0
    for ingredient in ingredients_data:
        ing_num = int(ingredient)
        # print(f"Checking ingredient number: {ing_num}")
        for row in fresh_data:
            nums = row.split("-")
            min_val = int(nums[0])
            max_val = int(nums[1])
            if min_val <= ing_num <= max_val:
                valid_count += 1
                # print(f"Ingredient {ing_num} is valid within range {min_val}-{max_val}")
                break # no need to check other ranges
    return valid_count


def solve_part2(data:list[str]) -> int:

    # Split data at the empty line, take the first part
    fresh_data = []
    for row in data:
        if row.strip() == "":
            break
        fresh_data.append(row)

    ranges = []
    for row in fresh_data:
        nums = row.split("-")
        min_val = int(nums[0])
        max_val = int(nums[1])
        ranges.append((min_val, max_val))
    # print(f"Parsed ranges: {ranges}")

    # Merge overlapping ranges
    ranges.sort(key=lambda x: x[0])  # Sort by the start of the range
    # print(f"Sorted ranges: {ranges}")
    merged_ranges = []
    curr_start, curr_end = ranges[0]
    for next_start, next_end in ranges[1:]:
        # print(f"Starting with range: {curr_start}-{curr_end}")
        # print(f"Comparing with next range: {next_start}-{next_end}")
        if next_start <= curr_end:
            curr_end = max(curr_end, next_end)  # Merge
            # print(f"Merged to new range: {curr_start}-{curr_end}")
        else:
            # print(f"Appending merged range: {curr_start}-{curr_end}")
            merged_ranges.append((curr_start, curr_end))
            curr_start, curr_end = next_start, next_end
    merged_ranges.append((curr_start, curr_end))  # Append the last range
    # print(f"Final merged ranges: {merged_ranges}")

    # Sum the sizes of the merged ranges
    total_size = sum(end - start + 1 for start, end in merged_ranges)
    # print(f"Total size of merged ranges: {total_size}")
    return total_size

if __name__ == "__main__":

    day_number = 5
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
    
