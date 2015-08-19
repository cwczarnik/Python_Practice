from numpy import array, arange,append
from pylab import plot,xlabel,ylabel,show
def f(r):
    x = r[0]
    y = r[1]
    dphi = y
    dubphi = (-x**-2)*(2*x*y + (x**2)*(y**2))
    
    return array([dphi,dubphi])


a = 0.0
b = 10.0
N = 1000
h = (b-a)/N

xpoints = arange(a,b,h)
xpoints = []
ypoints = []

r = array([1.0,1.0],float)

for x in xpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    k1 = h*f(r,x)
    k2 = h*f(r+0.5*k1,x+0.5*h)
    k3 = h*f(r+0.5*k2,x+0.5*h)
    k4 = h*f(r+k3,x+h)
    r += (k1+2*k2+2*k3+k4)/6
print sum(ypoints)
