# Cosine Similarity

## Definitions:

In some circumstances two vectors might be similar if they are pointing in the same direction even if they are of different lengths.
A measure of distance for this situation is the cosine of the angle between the two vectors. Just take the dot product of the two
vectors and divide by the two lengths. This measure is often used in natural language processing, recommendation systems, and clustering

Cosine Similarity is a metric used to measure the similarity between two non-zero vectors in a multidimensional space. 
It is often used in text analysis, recommendation systems, and clustering tasks because it quantifies how similar two objects are, 
regardless of their magnitude.

Similarity is a measure of resemblance, i.e., how similar or alike things being compared are. One way of computing similarity
is through the use of vectors. 

## Representing data sets as vectors (Understanding Vectors and Matrices)

1. **Matrix as a Table:**
   - A **matrix** is a structured arrangement of values (numbers, symbols, or expressions) organized in rows and columns.
   - A matrix with **r** rows and **c** columns has dimensions $r \times c$. 
   - In a **square matrix** (r = c), row and column counts are equal.

2. **Row and Column Vectors:**
   - **Row vectors** are single rows of a matrix, each of size $n = c$ (number of columns).
   - **Column vectors** are single columns of a matrix, each of size $n = r$ (number of rows).

3. **What is a Vector?**
   - A **vector** is an entity with:
     - **Magnitude:** The length of the vector.
     - **Direction:** The orientation in space.
   - A vector is represented mathematically as:
   
     $`\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix}`$
   
     where $`v_1, v_2, \ldots, v_n`$ are the vector's components.

4. **Visualization:**
   - For $n = 2$: Vectors can be represented in 2D space (e.g., $(x, y)$).
   - For $n = 3$: Vectors are visualized in 3D space (e.g., $(x, y, z)$).
   - For $n > 3$: Visualization is not possible, but vectors remain mathematically defined and computationally manageable.

    

### **Formula Definition**

The cosine similarity between two vectors $`\mathbf{A}`$ and $`\mathbf{B}`$ is defined as:

$`\text{Cosine Similarity} = \cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \|\mathbf{B}\|}`$

Where:
- $`\mathbf{A} \cdot \mathbf{B} = \sum_{i=1}^n A_i \cdot B_i`$: Dot product of $`\mathbf{A}`$ and $`\mathbf{B}`$.

- $`|\mathbf{A}\| = \sqrt{\sum_{i=1}^n A_i^2}`$: Magnitude of $`\mathbf{A}`$.

- $`\|\mathbf{B}\| = \sqrt{\sum_{i=1}^n B_i^2}`$: Magnitude of $`\mathbf{B}`$.


$`\cos(\theta)`$ ranges between:
- $1$: Perfect similarity (vectors are identical).
- $0$: Orthogonal vectors (no similarity).
- $-1$: Perfect dissimilarity (vectors are diametrically opposed).

---

### **Intuition**
Cosine similarity measures the cosine of the angle between two vectors:
- Smaller angles indicate higher similarity (closer vectors).
- Larger angles indicate lower similarity.

It focuses on the **direction** of vectors, not their magnitude, making it ideal for scenarios where magnitude 
differences (like text frequency counts) shouldn't affect similarity.

---

### **Applications**
1. **Text Mining**:
   - Compare document similarity based on term frequency-inverse document frequency (TF-IDF) vectors.
2. **Recommendation Systems**:
   - Compute user or item similarity based on preferences or attributes.
3. **Clustering**:
   - Measure pairwise similarities for clustering high-dimensional data.

---

### **Advantages**
- Magnitude-independent: Works well with sparse or high-dimensional data.
- Computationally efficient: Fast to compute with vectorized operations.

---

### **Example Calculation**
Let $`\mathbf{A} = [2, 3, 1]`$ and $`\mathbf{B} = [1, 0, 4]`$:

1. **Dot Product**:

   $`\mathbf{A} \cdot \mathbf{B} = (2 \cdot 1) + (3 \cdot 0) + (1 \cdot 4) = 2 + 0 + 4 = 6`$

2. **Magnitude**:
   $`\|\mathbf{A}\| = \sqrt{2^2 + 3^2 + 1^2} = \sqrt{4 + 9 + 1} = \sqrt{14}`$

   $`\|\mathbf{B}\| = \sqrt{1^2 + 0^2 + 4^2} = \sqrt{1 + 0 + 16} = \sqrt{17}`$


3. **Cosine Similarity**:
   
   $`\cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \|\mathbf{B}\|} = \frac{6}{\sqrt{14} \cdot \sqrt{17}} \approx 0.390`$


---

### **Comparison with Euclidean Distance**
While cosine similarity focuses on direction (angle), Euclidean distance measures magnitude-based differences. 
Both metrics can complement each other, depending on the dataset and the task.


Cosine similarity is a versatile tool in machine learning and data analysis, with its directional focus making it 
especially powerful for high-dimensional spaces.



### Reference
- Cosine Similarity Tutorial [Cosine Similarity Tutorial](https://itlab.uta.edu/courses/CSE5334-data-mining/current-offering/module-clustering/cosine-similarity-tutorial.pdf)
- What is Cosine Similarity: A Comprehensive Guide [What is Cosine Similarity: A Comprehensive Guide](https://www.datastax.com/guides/what-is-cosine-similarity)
- Understanding Cosine Similarity and Its Applications [Understanding Cosine Similarity and Its Applications](https://builtin.com/machine-learning/cosine-similarity)


















