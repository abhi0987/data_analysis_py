# varinace = the avg of the sqrd differnces from mean
# standard deviation = sqrt(variance)
import numpy as np
from scipy.stats import norm
from scipy.stats import expon
from scipy.stats import binom
from scipy.stats import poisson
import matplotlib.pyplot as plt
x = np.arange(-5,5,0.001)
y = np.arange(0,10,0.001)
z= np.arange(350,550,0.5)
#plt.plot(x,norm.pdf(x))
#plt.plot(y,binom.pmf(y,10,0.5))
#plt.plot(y,expon.pdf(y))
plt.plot(z,poisson.pmf(z,500))
plt.show()

