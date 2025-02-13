import sys

def print_stats(total_size, status_counts):
    """Prints the accumulated metrics."""
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        print(f"{code}: {status_counts[code]}")

total_size = 0
status_counts = {}
valid_statuses = {200, 301, 400, 401, 403, 404, 405, 500}

try:
    for i, line in enumerate(sys.stdin, 1):
        parts = line.split()
        if len(parts) < 7:
            continue
        
        try:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
        except ValueError:
            continue
        
        total_size += file_size
        if status_code in valid_statuses:
            status_counts[status_code] = status_counts.get(status_code, 0) + 1
        
        if i % 10 == 0:
            print_stats(total_size, status_counts)

except KeyboardInterrupt:
    print_stats(total_size, status_counts)
    raise

