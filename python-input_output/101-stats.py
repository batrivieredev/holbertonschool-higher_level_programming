#!/usr/bin/python3
import sys

"""
Log Parsing Script

This script reads input from stdin and computes metrics based on log lines.
The metrics include total file size and status code counts, which are printed
every 10 lines and after a keyboard interruption.

Attributes:
    valid_statuses (set): Set of valid HTTP status codes to track.
    total_size (int): Total size of all files in the log.
    status_counts (dict): Dictionary to count occurrences of each status code.
"""

valid_statuses = {200, 301, 400, 401, 403, 404, 405, 500}
total_size = 0
status_counts = {}

def print_stats(total_size, status_counts):
    """
    Prints the accumulated metrics (file size and status code counts).
    
    This function prints the total file size and the number of occurrences of each
    status code in the log, sorted by the status code.

    Args:
        total_size (int): The total accumulated file size.
        status_counts (dict): Dictionary containing status codes and their counts.

    Returns:
        None
    """
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        print(f"{code}: {status_counts[code]}")

try:
    # Read from stdin line by line
    for i, line in enumerate(sys.stdin, 1):
        parts = line.split()

        # Skip lines that do not have enough parts
        if len(parts) < 7:
            continue
        
        try:
            status_code = int(parts[-2])  # Extract status code
            file_size = int(parts[-1])    # Extract file size
        except ValueError:
            continue  # Skip lines with invalid number values
        
        total_size += file_size  # Accumulate file size
        
        # Count valid status codes
        if status_code in valid_statuses:
            status_counts[status_code] = status_counts.get(status_code, 0) + 1
        
        # Print stats every 10 lines
        if i % 10 == 0:
            print_stats(total_size, status_counts)

except KeyboardInterrupt:
    # Handle KeyboardInterrupt and print stats before exiting
    print_stats(total_size, status_counts)  # Print stats on keyboard interruption
    sys.exit(0)  # Gracefully exit after printing the stats

