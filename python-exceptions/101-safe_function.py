#!/usr/bin/python3

def safe_function(fct, *args):
    try:
        # Attempt to call the function with provided arguments
        return fct(*args)
    except Exception as e:
        # If an exception occurs, print the error message to stderr
        import sys
        print(f"Exception: {e}", file=sys.stderr)
        return None
