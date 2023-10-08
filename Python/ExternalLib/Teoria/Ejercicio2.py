import math as mt
from numpy import asarray
import numpy

print(mt.pi)

from math import *
print(pi, log(32, 2))

print(pi, log(32, 2))

print("numpy.random is a", type(numpy.random))
print("it contains names such as...",
      dir(numpy.random)[-15:]
     )

rolls = numpy.random.randint(low=1, high=6, size=10)
print(rolls)
print(type(rolls))
print(print(dir(rolls)))
print(rolls.mean())
print(rolls.tolist())

print(rolls + 10)
print(rolls <= 3)

xlist = [[1,2,3],[2,4,6],]
# Create a 2-dimensional array
x = numpy.asarray(xlist)
print("xlist = {}\nx =\n{}".format(xlist, x))

print(x[1,-1])