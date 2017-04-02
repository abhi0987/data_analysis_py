from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-3,3,0.001)

axes = plt.axes()
axes.set_xlim([-5,5])
axes.set_ylim([0,1.0])
axes.set_xticks(list(int(i) for i in range(-5,6)))
axes.set_yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])


axes.grid()
plt.xlabel('age')
plt.ylabel('food/day')

plt.plot(x,norm.pdf(x),'g-')
plt.plot(x,norm.pdf(x,1,0.5),'r--')




#plt.savefig('matplot.png',format='png')
plt.show()