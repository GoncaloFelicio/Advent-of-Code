from .shared import read_input
import time 


def solve_part1(data:list[str]) -> int:

    # pad with "." all around the matrix to avoid boundary checks
    width = len(data[0]) + 2
    padding_row = "." * width
    padded_data = [padding_row] + ["." + row + "." for row in data] + [padding_row]
    
    neighbor_counts_gr4 = 0
    # Calculate number of "@" neightbors for each cell
    for i in range(1, len(data) + 1): # for each row (excluding padding)
        # print(f"i={i}")
        row_counts = []
        for j in range(1, len(data[0]) + 1): # for each column (excluding padding)
            # print(f"j={j}")
            count = 0
            if padded_data[i][j] != "@":
                continue # only count neighbors for "@" cells
            else: 
                for dr in [-1, 0, 1]: # delta row, previous current and next
                    for dc in [-1, 0, 1]: # delta column, previous current and next
                        if dr == 0 and dc == 0:
                            continue # skip the cell itself
                        if padded_data[i + dr][j + dc] == "@":
                            # print("found @ at", i + dr, j + dc)
                            count += 1
                # print("count for cell", i, j, "is", count)
            if count < 4:
                # print("less than 4")
                neighbor_counts_gr4 += 1
                # print("incremented neighbor_counts_gr4 to", neighbor_counts_gr4)
    return neighbor_counts_gr4


def solve_part2(data:list[str]) -> int:
    # pad with "." all around the matrix to avoid boundary checks
    width = len(data[0]) + 2
    padding_row = "." * width
    padded_data = [padding_row] + ["." + row + "." for row in data] + [padding_row]
        
    def count_removable_paper(padded_data) -> int:
        # Function to count number of "@" cells with less than 4 "@" neighbors

        neighbor_counts_gr4 = 0
        # Calculate number of "@" neightbors for each cell
        for i in range(1, len(padded_data) - 1): # for each row (excluding padding)
            # print(f"i={i}")
            row_counts = []
            for j in range(1, len(padded_data[0]) - 1): # for each column (excluding padding)
                # print(f"j={j}")
                count = 0
                if padded_data[i][j] != "@":
                    continue # only count neighbors for "@" cells
                else: 
                    for dr in [-1, 0, 1]: # delta row, previous current and next
                        for dc in [-1, 0, 1]: # delta column, previous current and next
                            if dr == 0 and dc == 0:
                                continue # skip the cell itself
                            if padded_data[i + dr][j + dc] == "@":
                                # print("found @ at", i + dr, j + dc)
                                count += 1
                    # print("count for cell", i, j, "is", count)
                if count < 4:
                    # print("less than 4")
                    current_row = padded_data[i]
                    padded_data[i] = current_row[:j] + "." + current_row[j+1:]  # Remove the "@" cell
                    neighbor_counts_gr4 += 1
                    # print("incremented neighbor_counts_gr4 to", neighbor_counts_gr4)
        
        new_padded_data = padded_data
        return neighbor_counts_gr4, new_padded_data
    
    total_removed = 0
    while True:
        removed, padded_data = count_removable_paper(padded_data)
        if removed == 0:
            return total_removed
        total_removed += removed

if __name__ == "__main__":

    day_number = 4
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
    
