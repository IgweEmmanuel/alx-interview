#!/usr/bin/env python3
"""
utf-8 validation
"""

def validUTF8(data):
    """
    Number of bytes in the current UTF-8 character
    Args:
        data([]): data to check
    """
    num_bytes = 0

    # Masks to check the most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        mask = 1 << 7
        if num_bytes == 0:
            # Count the number of leading 1s in the current byte
            while byte & mask:
                num_bytes += 1
                mask >>= 1

            # For 1-byte character (ASCII), no additional bytes expected
            if num_bytes == 0:
                continue

            # If num_bytes is 1 or more than 4, it's invalid
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # If this byte is not starting with '10', it's invalid
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrement the count of remaining bytes
        num_bytes -= 1

    # If num_bytes is not zero, then we have leftover bytes, which is invalid
    return num_bytes == 0
