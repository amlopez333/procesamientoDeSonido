import numpy as np;
from matplotlib.pyplot import figure, plot, show
#signal function is as follows 
#s(t) = 1/4 + sum((-1 + (-1)^k)/(pi*k)^2 cos(2pi*k*f_0*t + pi))

#constants
a_0 = 1/4
pi = np.pi
samples = 10 #Samples to generate in interval for numpy linespace
def getAsubks(kMax):
    return [a_0] + [abs((-1 + (-1)**k)/(pi*k)**2) for k in range(1, kMax)]

def getCosine(theta, k, t, f_0):
    return np.cos(2*pi*k*f_0*t + theta)

def listToNPArray(array):
    return np.array(array)

def getIntervalSamples(Tmin, Tmax):
    return np.linspace(Tmin, Tmax, samples)
def calculateFourierSeriesCoefs(kMax, theta, T, Tmin, Tmax):
    f_0 = 1/T;
    A = listToNPArray(getAsubks(kMax))
    print(A)
    t_n = getIntervalSamples(Tmin, Tmax)
    cosines = [1] + [getCosine(theta, k, t_n[0], f_0) for k in range(1, kMax)]
    print(cosines)
    cosines = listToNPArray(cosines)
    return A, cosines, t_n


A, cosines, t_n = calculateFourierSeriesCoefs(10, pi, 1, -1/2,1/2)
array = np.multiply(A, cosines)
a = calculateFourierSeriesCoefs(10, pi, 1, -1/2,1/2)
print(t_n)
plot(t_n, array)
show()
