import timeit
import numpy as np
import scipy.optimize as optimize
import time

def f(x): 
    return np.cos(x)/(1.+x**2)

def fprime(x):
    return (-(x**2+1.)*np.sin(x)-2.*x*np.cos(x))/(x**2+1)**2

print ("time of calculations:")

# метод деления отрезка
start_time = time.time()
for i in  range (100):
	bisect_x = optimize.bisect(f, 0.1, 2.4)
print("bisect - %s sec" % (time.time() - start_time))

# метод Ньютона с заданием производной
start_time = time.time()
for i in  range (100):
	newton_x = optimize.newton(f, 1.2, fprime)
print("newton - %s sec" % (time.time() - start_time))

# метод секущих
start_time = time.time()
for i in  range (100):
	secant_x = optimize.newton(f, 1.2)
print("secant - %s sec" % (time.time() - start_time))

# метод Брента
start_time = time.time()
for i in  range (100):
	brentq_x = optimize.brentq(f, 0.1, 2.4)
print("brentq - %s sec" % (time.time() - start_time))
