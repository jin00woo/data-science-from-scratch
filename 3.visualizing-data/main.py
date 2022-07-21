from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# create a line chart, years on x-axis, gdp on y-axis
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
plt.title("Nominal GDP")
plt.ylabel("Billions of Dollars")
plt.xlabel("Year")
plt.show()

"""Bar Charts"""
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]
# plot bars with left x-coordinates [0, 1, 2, 3, 4], heights [num_oscars]
plt.bar(range(len(movies)), num_oscars)
plt.title("Top Movies")
plt.ylabel("Number of Awards")
plt.xticks(range(len(movies)), movies)
plt.show()

from collections import Counter
grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
histogram = Counter(min(grade//10 * 10, 90) for grade in grades)

plt.bar([x + 5 for x in histogram.keys()],
       histogram.values(),
       10,
       edgecolor=(0,0,0))
plt.axis([-5, 105, 0, 5])

plt.xticks([10 * i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Grades")
plt.show()

"""Misleading graphs"""
mentions = [500, 505]
years = [2017, 2018]

plt.bar(years, mentions, 0.8)
plt.xticks(years)
plt.ylabel("# of times I heard someone say 'data science'")

plt.ticklabel_format(useOffset=False)

plt.axis([2016.5, 2018.5, 499, 506])
plt.title("Look at the 'Huge' Increase!")
plt.show()

"""Scatterplots"""
friends = [ 70,  65,  72,  63,  71,  64,  60,  64,  67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)

for label, friend_count, minute_count in zip(labels, friends, minutes):
  plt.annotate(label, 
               xy = (friend_count, minute_count),
              xytext = (5, -5),
              textcoords = "offset points")

plt.title("Daily Minutes vs. Number of Friends")
plt.xlabel("# of Friends")
plt.ylabel("Daily minutes spent on site")
plt.show()

