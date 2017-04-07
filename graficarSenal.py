import numpy as np;
import matplotlib.pyplot as plt
#signal function is as follows 
#s(t) = 1/4 + sum((-1 + (-1)^k)/(pi*k)^2 cos(2pi*k*f_0*t + pi))

#constants
a_0 = 1/4
pi = np.pi
samples = 100 #Samples to generate in interval for numpy linespace

def getCks(kMax):
    return [(-1 + (-1)**k)/2*(pi *k)**2 for k in xrange(1,kMax)]

def complexToReal(cks):
    A = 2*np.abs(cks)
    theta = np.angle(cks)
    return A, theta

def graficar(A, theta, T, Tmin, Tmax):
    t_n = np.linspace(Tmin, Tmax, samples)
    f_0 = 1/T
    s_t = [0.0]*samples
    for i in range(samples):
        for j in range(len(A)):
            s_t[i] += A[j] * np.cos(2*pi*f_0*j*t_n[i] + theta)
    plt.plot(t_n, s_t)
    plt.show()
    return t_n, s_t

if __name__ == '__main__':
    cks = getCks(10)
    A, theta = complexToReal(cks)
    t, s = graficar(A, theta, 1, -1/2, 1/2)
    plt.plot(t,s)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.show()

