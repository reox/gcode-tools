#!/usr/bin/env python
# ----------------------------------------------------------------------------
#  "THE BEER-WARE LICENSE" (Revision 42):
# <hello@reox.at> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return  -Sebastian Bachmann 
# ----------------------------------------------------------------------------
import numpy

# CONFIGURATION # TODO use option parser....
# in mm


# mill head size
d = 6.0
# dimension in x,y and z
# x must be bigger then y!!! TODO: fix it...
x_dim = 120.0
y_dim = 60.0
z_dim = 3.0
# maximum insert into material in z direction
a_p = 3.0
# where should the mill be if not working in the material
safety_height = 40.0
# feed rate
f = 1800
# spindle speed
speed = 24000 


# PROGRAM START
radius = d/2.0
print "( milling a rectangle with size %f x %f with mill head radius %f)" %(x_dim, y_dim, radius)
print "G21 ;mm"
print "G90 ; absolute coordinates"
print "G64 ; continuous mode for corners"
print "G0 Z%f" %safety_height 
print "G0 X%f Y%f" %(x_dim/2.0, y_dim/2.0)
print "F%d" %f
print "(spindle warm up)"
print "M3 S6000"
print "G4 P60"
for s in list(numpy.arange(6000,speed+1, 6000))[1:]:
    print "S%d" %s
    print "G4 P60"
print "(program start)"
print "G54"

# 0|0 is the left lower corner

# x and y is the starting point (center of the rectangle)
x = x_dim/2.0
y = y_dim/2.0

# how much should be added per round in x direction
xa = radius

# how much should be added in y direction
# we calculate this by dividing the y_dim/2.0 by the count of runs needed in x (x_dim/2.0/xa)
runs_x = ((x_dim/2.0)-(x_dim/2.0)%radius)/xa
print "(we need %f runs in x direction)" %runs_x
ya = ((y_dim/2.0)-radius)/runs_x
# if ya < xa/2.0 --> special mode? TODO

if (x_dim/2.0)%radius == 0:
    end = (x_dim/2.0)-2.0*radius
else:
    end = (x_dim/2.0)-(x_dim/2.0)%radius-radius

depths = list(numpy.arange(-a_p,-z_dim, -a_p))
depths.append(-z_dim)
for z in depths:
# delta x and delta y, this is the delta from x and y (center)
    xd = 0
    yd = 0
    print "(New Depth %f)" %z
    print "G0 X%f Y%f" %(x,y)
    print "G1 Z%f" %z
    while xd < end:
        xd += xa
        yd += ya
        print "G1 X%f" %(x+xd)
        print "G1 Y%f" %(y+yd)
        print "G1 X%f" %(x-xd)
        print "G1 Y%f" %(y-yd)
        print "G1 X%f" %(x+xd)

# if extra material is left, we need to remove it.
    print "(extra pass)"
    print "G0 Z%f" %safety_height
    print "G0 X%f Y%f" %(radius, radius)
    print "G1 Z%f" %z
    print "G1 X%f" %(x_dim-radius)
    print "G1 Y%f" %(y_dim-radius)
    print "G1 X%f" %radius
    print "G1 Y%f" %radius 

    print "G0 Z%f" %safety_height


print "M30"
