import random as rand
from collections import Counter
# import matplotlib.pyplot as plt

num_friends = [rand.randint(0, 100) for i in range(100)]

friend_counts = Counter(num_friends)
xs = range(101)
ys = [friend_counts[x] for x in xs]
# plt.bar(xs, ys)
# plt.axis([0, 101, 0, 25])
# plt.title("Histogram of Friend Counts")
# plt.xlabel("# of friends")
# plt.ylabel("# of people")
# plt.show()

from typing import List

# Mean function
def mean(data: List[float]) -> float:
  return sum(data) / len(data)

# print(mean(num_friends))

# Median function
def _median_odd(data: List[float]) -> float:
  return sorted(data)[len(data) // 2]

def _median_even(data: List[float]) -> float:
  sorted_data = sorted(data)
  hi_midpoint = len(data) // 2
  return (sorted_data[hi_midpoint - 1] + sorted_data[hi_midpoint]) / 2

def median(data: List[float]) -> float:
  return _median_even(data) if len(data) % 2 == 0 else _median_odd(data)

assert median([1,2,5,9,10]) == 5
assert median([1,2,9,10]) == (2+9)/2

# print(median(num_friends))

# Quantile
def quantile(data: List[float], p: float) -> float:
  p_index = int(p * len(data))
  return sorted(data)[p_index]

# print(quantile(num_friends, 0.25))

# Mode
def mode(data: List[float]) -> float:
  counts = Counter(data)
  max_count = max(counts.values())
  return [x_i for x_i, count in counts.items() if count == max_count]

# print(mode(num_friends))

# Range
def data_range(data: List[float]) -> float:
  return max(data) - min(data)

def interquartile_range(data: List[float]) -> float:
  return quantile(data, 0.75) - quantile(data, 0.25)

# Variance
def de_mean(data: List[float]) -> List[float]:
  x_bar = mean(data)
  return [x - x_bar for x in data]

def sum_of_squares(data: List[float]) -> float:
  return sum(element**2 for element in data)

def variance(data: List[float]) -> float:
  assert len(data) >= 2, "at least two elements required"
  n = len(data)
  deviations = de_mean(data)
  return sum_of_squares(deviations) / (n-1)

# Standard deviation
import math

def standard_deviation(data: List[float]) -> float:
  return math.sqrt(variance(data))

# Covariance
def dot(x: List[float], y: List[float]) -> float:
  return sum(x_i * y_i for x_i, y_i in zip(x,y))

def covariance(x: List[float], y: List[float]) -> float:
  assert len(x) == len(y), "Two data sets must have same number of elements"

  return dot(de_mean(x), de_mean(y)) / (len(x) - 1)

# Correlation
def correlation(x: List[float], y: List[float]) -> float:
  stdev_x = standard_deviation(x)
  stdev_y = standard_deviation(y)
  if stdev_x > 0 and stdev_y > 0:
    return covariance(x,y) / stdev_x / stdev_y
  else:
    return 0