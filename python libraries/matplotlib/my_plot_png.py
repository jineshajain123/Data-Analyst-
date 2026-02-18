import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot
plt.figure(figsize=(8, 4)) 

# X and Y labels
plt.style.use('_mpl-gallery')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.plot(x, y, label='Sine Wave')
plt.title('Sine Wave Plot')
plt.savefig("plot.png")
plt.savefig('my_plot.pdf')
plt.show()