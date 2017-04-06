import numpy as np;
from matplotlib.pyplot import figure, plot, show
#signal function is as follows 
#s(t) = 1/4 + sum((-1 + (-1)^k)/(pi*k)^2 cos(2pi*k*f_0*t + pi))

#cosntants
a_0 = 1/4
pi = np.pi
def getAsubks(kMax):
    return [(-1 + (-1)**k)/(pi*k)**2 for k in xrange(1, kMax)]

def getCosine(theta, k, t, f_0):
    return np.cos(2*pi*k*f_0*t + theta)

def listToNPArray(list):
    return np.array(list)

def calculateFourierSeriesCoefs(kMax, theta, t, T):
    f_0 = 1/T;
    A = listToNPArray(getAsubks(kMax))
    cosines = [getCosine(theta, k, t, f_0) for k in xrange(1, kMax)]
    cosines = listToNPArray(cosines)
    return A, cosines

print calculateFourierSeriesCoefs(10, pi, -1/2, 1)

