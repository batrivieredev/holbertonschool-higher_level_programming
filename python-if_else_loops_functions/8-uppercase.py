#!/usr/bin/python3
def uppercase(str):
    for char in str:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert to uppercase by adjusting ASCII value
            char = chr(ord(char) - 32)
        print(char, end="")
    print()
