#!/usr/bin/env python3
"""
Mission 5: Interactive Number Converter
Converts a user-provided decimal number into Binary and Hexadecimal.
"""

def main():
    print("====================================")
    print(" Digital Detective Number Converter ")
    print("====================================")
    
    try:
        user_input = input("Enter a positive decimal integer: ").strip()
        decimal_val = int(user_input)
        
        if decimal_val < 0:
            print("Please enter a positive integer.")
            return

        binary_rep = bin(decimal_val)       # e.g. '0b1101'
        hex_rep = hex(decimal_val).upper()  # e.g. '0X1F'
        hex_formatted = "0x" + hex_rep[2:]

        print(f"\nResults for decimal {decimal_val}:")
        print(f" - Binary representation      : {binary_rep} ({binary_rep[2:]})")
        print(f" - Hexadecimal representation : {hex_formatted}")
    except ValueError:
        print("Invalid input! Please enter digits only.")

if __name__ == "__main__":
    main()
