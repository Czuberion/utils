#!/usr/bin/env python
import sys
import ast

def extract_value_from_dict(key):
    # Read input from standard input
    input_str = sys.stdin.read()

    # Convert the input string to a dictionary
    try:
        dict_data = ast.literal_eval(input_str.strip())
    except (SyntaxError, ValueError) as e:
        print(f"Error converting input to a dictionary: {e}", file=sys.stderr)
        sys.exit(1)

    # Extract value using the provided key
    if key in dict_data:
        print(dict_data[key])
    else:
        print(f"Key '{key}' not found in dictionary.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_key.py <key>")
        sys.exit(1)
    extract_value_from_dict(sys.argv[1])

