#!/usr/bin/python3
"""
utf-8 validation
"""


def validUTF8(data):
    """
    Number of bytes in the current UTF-8 character
    Args:
        data([]): data to check
    """
    next_bits = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for item in data:
        mask = 1 << 7

        if next_bits == 0:

            while item & mask:
                next_bits += 1
                mask >>= 1

            if next_bits == 0:
                continue
            if next_bits == 1 or next_bits > 4:
                return False
        elif not (item & mask1 and not (item & mask2)):
            return False
        next_bits -= 1
    return next_bits == 0
