# 0x07-rotate_2d_matrix

This project contains a function to rotate a 2D matrix by 90 degrees clockwise.

## Function

### rotate_2d_matrix

Rotates a given n x n 2D matrix 90 degrees clockwise in place.

#### Parameters

- `matrix` (list of list of int): The 2D matrix to rotate.

#### Returns

- `None`: The matrix is rotated in place.

## Usage

To use the function, import it and call it with a 2D matrix:

```python
from 0-rotate_2d_matrix import rotate_2d_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_2d_matrix(matrix)
print(matrix)  # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
