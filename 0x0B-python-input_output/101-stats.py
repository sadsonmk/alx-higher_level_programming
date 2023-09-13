#!/usr/bin/python3
"""a module that reads stdin line by line and computes metrics"""
import sys


def read_metrics(size, status_code):
    """a script that reads stdin line by line and computes metrics"""
    
    sorted_codes = sorted(status_code)
    print(f"File size: {size}")
    for code in sorted_codes:
        print(f"{code}: {sorted_codes[code]}")
