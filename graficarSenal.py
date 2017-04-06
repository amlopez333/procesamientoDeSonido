import numpy as np;
from matplotlib.pyplot import figure, plot, show
#signal function is as follows 
#s(t) = 1/4 + sum((-1 + (-1)^k)/(pi*k)^2 cos(2pi*k*f_0*t + pi))

#constants
a_0 = 1/4
pi = np.pi
samples = 100 #Samples to generate in interval for numpy linespace
def getAsubks(kMax):
    return [abs((-1 + (-1)**k)/(pi*k)**2) for k in xrange(1, kMax)]

def getCosine(theta, k, t, f_0):
    return np.cos(2*pi*k*f_0*t + theta)

def listToNPArray(list):
    return np.array(list)

def getIntervalSamples(Tmin, Tmax):
    return np.linspace(Tmin, Tmax, samples)
def calculateFourierSeriesCoefs(kMax, theta, T, Tmin, Tmax):
    f_0 = 1/T;
    A = listToNPArray(getAsubks(kMax))
    t_n = getIntervalSamples(Tmin, Tmax)
    cosines = [getCosine(theta, k, t, f_0) for k in xrange(1, kMax)]
    cosines = listToNPArray(cosines)
    return A, cosines

print calculateFourierSeriesCoefs(10, pi, -1/2, 1)

