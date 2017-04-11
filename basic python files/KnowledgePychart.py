import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

fromarea = ['Travelling','books','video gaming','as introvert']
knowledge = [60,20,8,2]
colors = ['r','g','b','m']

#plt.pie(knowledge,colors=colors,labels=fromarea,explode=None)

plt.title('Human knowledge')


plt.bar(range(len(knowledge)),knowledge,color = colors)
plt.show()
