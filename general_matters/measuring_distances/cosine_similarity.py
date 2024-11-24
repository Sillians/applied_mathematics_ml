import numpy as np

# Using Numpy for basic operations like dot product and vector norms
def cosine_similarity(vector_a, vector_b):
    """
    Calculate cosine similarity between two vectors.
    """
    dot_product = np.dot(vector_a, vector_b)
    magnitude_a = np.linalg.norm(vector_a)
    magnitude_b = np.linalg.norm(vector_b)
    if magnitude_a == 0 or magnitude_b == 0:
        return 0  # Handle zero vectors to avoid division by zero
    return dot_product / (magnitude_a * magnitude_b)

# Example
vector_a = np.array([2, 3, 1])
vector_b = np.array([1, 0, 4])
similarity = round(cosine_similarity(vector_a, vector_b), 2)
print(f"Cosine Similarity: {similarity}")




# Implementation from Scratch
# Calculate the dot product of two vectors.
def dot_product(vector_a, vector_b):
    return sum(a * b for a, b in zip(vector_a, vector_b))

# Calculate the magnitude of a vector.
def vector_magnitude(vector):
    return sum(x ** 2 for x in vector) ** 0.5

# Calculate cosine similarity between two vectors without using libraries.
def cosine_similarity(vector_a, vector_b):

    dot = dot_product(vector_a, vector_b)
    magnitude_a = vector_magnitude(vector_a)
    magnitude_b = vector_magnitude(vector_b)
    if magnitude_a == 0 or magnitude_b == 0:
        return 0  # Handle zero vectors to avoid division by zero
    return dot / (magnitude_a * magnitude_b)

# Example
vector_a = [2, 3, 1]
vector_b = [1, 0, 4]
similarity = round(cosine_similarity(vector_a, vector_b), 2)
print(f"Cosine Similarity: {similarity}")







# Man they need to facilitate the guys on lizzo so kai can get the iso
