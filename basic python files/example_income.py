import numpy as np
import matplotlib.pyplot as plt 
from scipy import stats
incomes = np.random.normal(27000,15000,10000)
incomes = np.append(incomes,[1000000000])
ages = np.random.randint(10000,high=90000,size=500)
ages = np.append(ages,[90000000])
print(stats.mode(ages))
print('median:'+str(np.median(ages)))
print('mean:'+str(np.mean(ages)))
plt.hist(ages,50)
plt.show()