#!/usr/bin/python3
"""lockboxes to determine if
 if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines whether all the boxes in the list can be opened.
    """
    num_boxes = len(boxes)
    unlcked_boxes = [False] * num_boxes
    unlcked_boxes[0] = True

    # Use a stack to keep track of boxes that we can currently unlock
    lines = [0]

    while lines:
        box_num = lines.pop()
        box = boxes[box_num]
        for key in box:
            # Check that the key corresponds to a valid box and that the box hasn't already been unlocked
            if key < num_boxes and not unlcked_boxes[key]:
                unlcked_boxes[key] = True
                lines.append(key)

    return all(unlcked_boxes)
