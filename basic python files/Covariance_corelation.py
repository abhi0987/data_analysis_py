#first take 2 vectors : lets age vs income
#find the 2 variance vectors from means of the original vectors
#take the dot product(cosine of angle) of 2 variance vectors
#divide by the sample size
#  That is covarinace
import numpy as np
import matplotlib.pyplot as plt


def de_mean(x):
    xmean = np.mean(x)
    xnew = [xi - xmean for xi in x]
    return xnew

def covariance(x,y):
    n = len(x)
    dot_ = (np.dot(de_mean(x),de_mean(y)))/(n-1)
    return dot_


pagespeed = np.random.normal(3.0,1.0,1000)
purchaseamnt = np.random.normal(50.0,10.0,1000)

plt.scatter(pagespeed,purchaseamnt)
print covariance(pagespeed,purchaseamnt)
plt.show()

