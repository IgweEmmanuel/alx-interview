#!/usr/bin/env python3
"""Unlock box"""


def canUnlockAll(boxes):
    n = len(boxes)
    opened = [False] * n
    opened[0] = True  # The first box is always open
    keys = [0]  # Start with the key to the first box

    while keys:
        key = keys.pop()
        for new_key in boxes[key]:
            if new_key < n and not opened[new_key]:
                opened[new_key] = True
                keys.append(new_key)
    
    return all(opened)
