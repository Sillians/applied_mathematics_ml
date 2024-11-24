# Euclidean Distance

The Euclidean metric (and distance magnitude) is that which corresponds to everyday experience and
perceptions. That is, the kind of $1$, $2$, and $3‐Dimensional$ linear metric world where the distance between
any two points in space corresponds to the length of a straight line drawn between them.

The **Euclidean Distance** is a measure of the straight-line distance between two points in Euclidean space. 
It is one of the most commonly used metrics in mathematics, machine learning, and data analysis for measuring 
similarity or dissimilarity between data points.


The summation formula for the Euclidean distance between two points $`A(x_1, y_1, z_1, \ldots)`$ and $`B(x_2, y_2, z_2, \ldots)`$
in $n$-dimensional space is:

$`d(A, B) = \sqrt{\sum_{i=1}^n (p_{i, B} - p_{i, A})^2}`$

### Explanation:
1. $n$ is the number of dimensions.
2. $`p_{i, A}`$ and $`p_{i, B}`$ represent the coordinates of points $A$ and $B$ in the $i-th$ dimension.
3. The formula calculates the square root of the sum of squared differences between corresponding coordinates of $A$ and $B$.

For example:
- In **2D**: $A(x_1, y_1)$, $B(x_2, y_2)$:

  $`d(A, B) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}`$


- In **3D**: $`A(x_1, y_1, z_1)`$, $`B(x_2, y_2, z_2)`$:
  
  $`d(A, B) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}`$


---

### **Example 1.0**

Here’s how the Euclidean distances between the three persons, calculated step by step using the provided formula:

### Formula:

$`d = \sqrt{\sum_{i=1}^v (p_{i,2} - p_{i,1})^2}`$

Where:
- $v$ is the number of variables (dimensions).
- $`p_{i,1}, p_{i,2}`$ are the scores of persons 1 and 2 on variable $i$.

---

### **Calculations**:

#### Distance Between Person 1 and Person 2:
Given scores:
- Person 1: $(20, 80)$
- Person 2: $(30, 44)$

$`d = \sqrt{(30 - 20)^2 + (44 - 80)^2}`$

$`d = \sqrt{10^2 + (-36)^2}`$

$`d = \sqrt{100 + 1296} = \sqrt{1396} \approx 37.36`$

---

#### Distance Between Person 1 and Person 3:
Given scores:
- Person 1: $(20, 80)$
- Person 3: $(90, 40)$

$`d = \sqrt{(90 - 20)^2 + (40 - 80)^2}`$

$`d = \sqrt{70^2 + (-40)^2}`$

$`d = \sqrt{4900 + 1600} = \sqrt{6500} \approx 80.62`$

---

#### Distance Between Person 2 and Person 3:
Given scores:
- Person 2: $`(30, 44)`$
- Person 3: $`(90, 40)`$

$`d = \sqrt{(90 - 30)^2 + (40 - 44)^2}`$

$`d = \sqrt{60^2 + (-4)^2}`$

$`d = \sqrt{3600 + 16} = \sqrt{3616} \approx 60.13`$

---

### Final Distances:
- $`d_{1,2} = 37.36`$
- $`d_{1,3} = 80.62`$
- $`d_{2,3} = 60.13`$


---

### **Applications**
1. **Machine Learning**: Used in algorithms like `K-Nearest Neighbors (KNN)` for measuring similarity between data points.
2. **Computer Graphics**: Determines the shortest path between two points in 2D or 3D space.
3. **Physics**: Represents the straight-line distance between objects.
4. **Data Analysis**: Measures dissimilarity between features in datasets.
5. **Robotics/Path Planning**: Determines the direct path between positions.

---

### **Key Properties**
1. **Non-Negativity**: $`d \geq 0`$ (distance is always non-negative).
2. **Symmetry**: $`d(P_1, P_2) = d(P_2, P_1)`$ (distance from $P_1$ to $P_2$ equals distance from $P_2$ to $P_1$).
3. **Identity**: $`d(P_1, P_2) = 0 \iff P_1 = P_2`$ (distance is zero if and only if the points are identical).
4. **Triangle Inequality**: $`d(P_1, P_3) \leq d(P_1, P_2) + d(P_2, P_3)`$ (straight line is the shortest path).

---

### **Example 2.0**
Find the Euclidean distance between $`P_1(2, 3)`$ and $`P_2(5, 7)`$ in 2D:

$`d = \sqrt{(5 - 2)^2 + (7 - 3)^2} = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5`$

---

### **Generalization**
1. **Weighted Euclidean Distance**:
   Adds weights to the dimensions:

   $`d = \sqrt{\sum_{i=1}^n w_i (x_{i2} - x_{i1})^2}`$

2. **Normalized Euclidean Distance**:
   Accounts for scaling or normalization:

   $`d = \sqrt{\sum_{i=1}^n \frac{(x_{i2} - x_{i1})^2}{\sigma_i^2}}`$

   where $\sigma_i$ is the standard deviation of the $i-th$ feature.

---

### **Extensions**
1. **Euclidean Distance in Feature Space**:
   In machine learning, the distance metric is used in high-dimensional space for clustering, classification, and anomaly detection.

2. **Alternative Metrics**:
   In scenarios where Euclidean distance is not suitable, consider:
   - **Manhattan Distance**: Uses absolute differences.
   - **Cosine Similarity**: Measures the cosine of the angle between vectors.
   - **Minkowski Distance**: A generalized form.

Euclidean distance remains the foundation for numerous spatial computations, making it essential to understand its applications
and limitations in complex systems.




### Reference
- Euclidean Distance Matrix [Euclidean Distance Matrix](https://ccrma.stanford.edu/~dattorro/EDM.pdf)
- Euclidean Distance Matrices and Applications [Euclidean Distance Matrices and Applications](https://www.math.uwaterloo.ca/~hwolkowi/henry/reports/EDMhandbook.pdf)
- Euclidean Distance raw, normalized, and double‐scaled coefficients [Euclidean Distance raw, normalized, and double‐scaled coefficients](https://www.pbarrett.net/techpapers/euclid.pdf)


