import os

INPUTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")


def read_input(day_number: int, filename: str = None) -> list[str]:

    if filename is None:
        filename = f"day{day_number:02d}_input.txt"
    
    filepath = os.path.join(INPUTS_DIR, filename)

    try:
        print(f"Reading input from {filepath}")
        with open(filepath, "r") as f:
            # Read all lines and strip whitespace
            data = [line.strip() for line in f]
        return data
    
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return []
    
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []

