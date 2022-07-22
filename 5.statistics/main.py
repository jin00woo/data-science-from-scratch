import random as rand
from collections import Counter
import matplotlib.pyplot as plt

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

def mean(data: List[float]) -> float:
  return sum(data) / len(data)

print(mean(num_friends))