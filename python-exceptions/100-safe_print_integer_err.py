#!/usr/bin/python3

def safe_print_integer_err(value):
    try:
        # Try to print the value using the format function
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        # If a ValueError or TypeError occurs, print the exception to stderr
        import sys
        print("Exception:", e, file=sys.stderr)
        return False
