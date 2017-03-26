from math import hypot, atan2, sin, cos
from random import randint
from time import clock

interval = 100000
GM = 500
res = 0
x_acc = 0
y_acc = 0

time0 = clock()
for _ in range(interval):
    x = randint(0,1000)
    y = randint(0,1000)
    acc = -GM/hypot(x,y)**3
    x_acc = acc * x
    y_acc = acc * y
print(clock()-time0,'seconds')

time1 = clock()
for _ in range(interval):
    x = randint(0,1000)
    y = randint(0,1000)
    theta = atan2(y,x)
    g = -GM/(x**2+y**2)
    x_acc = cos(theta)*g
    y_acc = sin(theta)*g
print(clock()-time1,'seconds')

##for _ in range(50):
##    x = randint(0,1000)
##    y = randint(0,1000)
##    acc = -GM/hypot(x,y)**3
##    x_acc = acc * x
##    y_acc = acc * y
##    theta = atan2(y,x)
##    g = -GM/(x**2+y**2)
##    x_acc2 = cos(theta)*g
##    y_acc2 = sin(theta)*g
##    print(x,'results in a difference of',x_acc-x_acc2)
