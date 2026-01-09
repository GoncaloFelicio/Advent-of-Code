import os

INPUTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")


def read_input(day_number: int, filename: str = None) -> list[str]:

    if filename is None:
        filename = f"day{day_number:02d}_input.txt"
    
    filepath = os.path.join(INPUTS_DIR, filename)

    try:
        print(f"Reading input from {filepath}")
        with open(filepath, "r") as f:
            # Read all lines without stripping whitespaces
            data = [line for line in f]

            if len(data) == 1 and ',' in data[0]:
                print("Detected single-line, comma-separated format.")
                content = data[0]
                # Split the single line by comma without stripping whitespace from each item
                data = [item for item in content.split(',')]
            else:
                print("Detected multi-line format.")
                # If it's multi-line, or a single line without a comma, the base read is correct.
                data = data
                
        return data
    
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return []
    
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []

