import os
import sys


def process_data(data=[]):
    unused_variable = 42
    try:
        total = 0
        for value in data:
            total = total + value
        return total
    except:
        pass


def main():
    numbers = [1, 2, 3]
    result = process_data(numbers)
    print("Total:", result)
    print("This line is intentionally very long so that the static analysis tool reports a line length violation in its report")


if __name__ == "__main__":
    main()
