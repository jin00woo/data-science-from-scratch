# Functions necessary for vector operations, created using lists, as an alternative to those of Numpy. 

import math

def add(v, w):
    assert len(v) == len(w), "Vectors should have the same length"
    return [v_i + w_i for v_i, w_i in zip(v,w)]

def subtract(v,w):
    assert len(v) == len(w), "Vectors should have the same length"
    return [v_i - w_i for v_i, w_i in zip(v,w)]

def vector_sum(vectors):
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "Vectors should have the same length"
    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]

def scalar_multiply(constant, vector):
    return [c * v_i for v_i in vector]

def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def dot(v, w):
    assert len(v) == len(w), "Vectors should have the same length"
    return sum(v_i * w_i for v_i, w_i in zip(v,w))

def sum_of_squares(v):
    return dot(v,v)

def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def squared_distance(v, w):
    return sum_of_squares(subtract(v,w))

def distance(v, w):
    return magnitude(subtract(v,w))
