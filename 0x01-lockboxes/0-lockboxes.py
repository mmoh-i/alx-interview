#!/usr/bin/python3
"""lockboxes to determine if
 if all the boxes can be opened.
"""
from typing import List

def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Determines whether all the boxes in the list can be opened.
    """
    num_boxes = len(boxes)
    unlcked_boxes = [False] * num_boxes
    unlcked_boxes[0] = True

    # Use a stack to keep track of boxes that we can currently unlock
    stack = [0]

    while stack:
        box_num = stack.pop()
        box = boxes[box_num]
        for key in box:
            # Check that the key corresponds to a valid box and that the box hasn't already been unlocked
            if key < num_boxes and not unlocked_boxes[key]:
                unlcked_boxes[key] = True
                stack.append(key)

    return all(unlocked_boxes)
