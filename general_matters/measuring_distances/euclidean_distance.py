import math
import numpy as np
from typing import Optional, List

def euclidean_distance(point1: Optional[list | tuple], point2: Optional[list | tuple]) -> float:
    """
    :param point1: Tuple or list representing the coordinates of the first point.
    :param point2: Tuple or list representing the coordinates of the second point.
    :return: Euclidean distance between the two points.
    """

    # Ensure same dimension of both points
    if len(point1) != len(point2):
        raise ValueError("Points must have the same number of dimensions")

    # Compute sum squared differences
    squared_difference_sum = sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2))

    # Get the square root of the sum
    return round(math.sqrt(squared_difference_sum), 2)


# Define the points
person1 = (20, 80)
person2 = [30, 44]
person3 = (90, 40)

# Calculate distances
d_1_2 = euclidean_distance(person1, person2)
d_2_3 = euclidean_distance(person2, person3)
print(d_1_2, d_2_3)



# Efficient Handling for Large Matrices
"""
If dealing with large matrices where pairwise distances need to be computed:

- Use vectorized operations with libraries like NumPy for efficiency.
- Avoid nested loops, as they can be slow for large data.
"""


def euclidean_distance_matrix(matrix: np.array) -> float:
    """

    :param matrix: A 2D Numpy array where each row is a data point
    :return: A 2D Numpy array containing pairwise Euclidean distances
    """

    # Get the squared norms of each row
    squared_norms = np.sum(matrix ** 2, axis=1)

    # Compute the pairwise squared distances using broadcasting
    squared_distances = (
            squared_norms[:, np.newaxis] + squared_norms[np.newaxis, :] - 2 * np.dot(matrix, matrix.T)
    )

    # Ensure no negative values due to floating-point errors
    squared_distances = np.maximum(squared_distances, 0)
    return np.sqrt(squared_distances)


# Define a large matrix (each row is a data point)
matrix = np.array([
    [20, 80],
    [30, 44],
    [90, 40],
])

# Calculate pairwise distances
distance_matrix = euclidean_distance_matrix(matrix)

# Print the result
print("Pairwise Euclidean Distance Matrix:")
print(distance_matrix)






















