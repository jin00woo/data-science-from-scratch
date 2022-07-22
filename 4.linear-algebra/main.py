from typing import List

Vector = List[float]

height_weight_age = [70, 170, 40]
grades = [95, 80, 75, 62]

# Add function
def add(v: Vector, w: Vector) -> Vector:
  assert len(v) == len(w), "vectors must be same length"
  return [v_i + w_i for v_i, w_i in zip(v,w)]

assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]

# Subtract function
def subtract(v: Vector, w: Vector) -> Vector:
  assert len(v) == len(w), "vectors must be same length"
  return [v_i - w_i for v_i, w_i in zip(v,w)]

assert subtract([3, 2, 1], [3, 2, 1]) == [0, 0, 0]

# Componentwise-add function
def vector_sum(vectors: List[Vector]) -> Vector:
  assert vectors, "No vectors provided"
  num_elements = len(vectors[0])
  assert all(len(v) == num_elements for v in vectors), "Vectors have different lengths"
  return [sum(vector[i] for vector in vectors) for i in range(num_elements)]

assert vector_sum([[1,2],[3,4],[5,6]]) == [9,12]

# Scalar multiplication function
def scalar_multiply(c: float, v: Vector) -> Vector:
  return [c * v_i for v_i in v]

assert scalar_multiply(2, [1,2]) == [2,4]

# Vector mean function
def vector_mean(vectors: List[Vector]) -> Vector:
  n = len(vectors)
  return scalar_multiply(1/n, vector_sum(vectors))

assert vector_mean([[1,2], [3,4]]) == [2,3]

# Dot multiplication function
def dot(v: Vector, w: Vector) -> float:
  assert len(v) == len(w), "Vectors must be same length"
  return sum(v_i * w_i for v_i, w_i in zip(v,w))

assert dot([1,2,3], [4,5,6]) == 32

# Sum of squares
def sum_of_squares(v: Vector) -> float:
  return dot(v,v)

assert sum_of_squares([1,2,3]) == 14

# Magnitude function
import math

def magnitude(v: Vector) -> float:
  return math.sqrt(sum_of_squares(v))

assert magnitude([3,4]) == 5

# Distance
def distance(v: Vector, w: Vector) -> float:
  return magnitude(subtract(v,w))

# Matrices
Matrix = List[List[float]]

from typing import Tuple

# Matrix shape
def shape(A: Matrix) -> Tuple[int, int]:
  num_rows = len(A)
  num_cols = len(A[0]) if A else 0
  return num_rows, num_cols

assert shape([[1,2,3], [4,5,6]]) == (2,3)

# Matrix row & column
def get_row(A: Matrix, i: int) -> Vector:
  return A[i]

def get_column(A: Matrix, j: int) -> Vector:
  return [A_i[j] for A_i in A]

# Matrix generator
from typing import Callable

def make_matrix(num_rows: int, num_cols: int, entry_fn: Callable[[int,int], float]) -> Matrix:
  return [[entry_fn(i, j)
          for j in range(num_cols)]
          for i in range(num_rows)]

def identity_matrix(n: int) -> Matrix:
  return make_matrix(n, n, lambda i, j: 1 if i == j else 0)

assert identity_matrix(3) == [
  [1, 0, 0],
  [0, 1, 0],
  [0, 0, 1]
]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

"""Above can also be represented as below"""

#            user 0  1  2  3  4  5  6  7  8  9
#
friend_matrix = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # user 0
                 [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],  # user 1
                 [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # user 2
                 [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],  # user 3
                 [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],  # user 4
                 [0, 0, 0, 0, 1, 0, 1, 1, 0, 0],  # user 5
                 [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],  # user 6
                 [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],  # user 7
                 [0, 0, 0, 0, 0, 0, 1, 1, 0, 1],  # user 8
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]  # user 9

assert friend_matrix[0][2] == 1, "0 and 2 are friends"
assert friend_matrix[0][8] == 0, "0 and 8 are not friends"

# Checking a node's connections
friends_of_five = [i for i, is_friend in enumerate(friend_matrix[5]) if is_friend]

assert len(friends_of_five) == 3, "User 5 has 3 friends"
