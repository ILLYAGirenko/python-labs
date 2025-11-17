import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 100)
y = 2**x * np.sin(10 * x)
plt.plot(x, y, label='2^x*sin(10x)', color = "red", linewidth = 5)
plt.title('My plot', fontsize=15)
plt.xlabel('x', fontsize=12, color='blue')
plt.ylabel('y', fontsize=12, color='blue')
plt.legend()
plt.show()
plt.grid(True)