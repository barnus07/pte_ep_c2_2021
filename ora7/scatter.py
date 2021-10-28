from matplotlib.pyplot import *
import numpy as np
number_of_points = 100000
x = np.random.randint(0, 100, number_of_points)
y = x + 10*np.random.randn(number_of_points)
sizes = np.random.randint(0, 200, number_of_points)
colors = np.random.randint(0,10, number_of_points)
scatter(x, y, s=sizes, c=colors)
show()

