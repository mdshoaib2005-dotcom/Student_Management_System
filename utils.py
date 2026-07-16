import os

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header(title):
    """Print a formatted section header."""
    print()
    print("=" * 60)
    print(title.center(60))
    print("=" * 60)


def print_table(headers, rows):
    """Print data in a table format."""

    col_widths = [len(h) for h in headers]

    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))

    separator = "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"

    print(separator)

    header = "|"
    for i, h in enumerate(headers):
        header += f" {h:<{col_widths[i]}} |"

    print(header)
    print(separator)

    for row in rows:
        line = "|"
        for i, cell in enumerate(row):
            line += f" {str(cell):<{col_widths[i]}} |"
        print(line)

    print(separator)


def get_valid_input(prompt, input_type=str, min_val=None, max_val=None):
    """Ask until valid input is entered."""

    while True:
        try:
            value = input_type(input(prompt))

            if min_val is not None and value < min_val:
                print(f"Value must be at least {min_val}")
                continue

            if max_val is not None and value > max_val:
                print(f"Value must be at most {max_val}")
                continue

            return value

        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")

#Test Code
if __name__ == "__main__":
    print_header("TEST HEADER")

    headers = ["ID", "Name", "Age"]
    rows = [
        ["S001", "Rahul", 20],
        ["S002", "Priya", 19]
    ]

    print_table(headers, rows)
