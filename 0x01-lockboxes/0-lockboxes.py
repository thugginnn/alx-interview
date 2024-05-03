#!/usr/bin/python3
"""
Determines if all lockboxes can be opened.
"""

def canUnlockAll(boxes):
    """
    Determines if all lockboxes can be opened.

    Args:
        boxes (list): A list of lists showing the lockboxes and their
        corresponding keys.

    Returns:
        bool: True if all lockboxes can be opened, False otherwise.
    """
    # Set to keep track of visited boxes
    visited = set()
    #Queue to keep track of boxes to visit
    queue = [0]

    # Loop until the queue is empty
    while queue:
        # Pop the first box from the queue
        current_box = queue.pop(0)
        # Mark the box as visited
        visited.add(current_box)
        # Get the keys in the current box
        keys = boxes[current_box]
        # Comb through the keys
        for key in keys:
            # If the keys opens a new box and hasn't been visited yet
            if key < len(boxes) and key not in visited:
                # Add the new box to the queue
                queue.append(key)

    # If all boxes have been visited, return True
    return len(visited) == len(boxes)


if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1,4,6], [2], [0, 4, 1], [5, 6, 2], [3], [4,1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2],[0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll))
