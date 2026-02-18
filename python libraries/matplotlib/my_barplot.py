import matplotlib.pyplot as plt
import numpy as np


categories = ["A", "B", "C"]
values = [12, 44, 53]

plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.bar(categories, values)
plt.show()