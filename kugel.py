#!/usr/bin/env python
# ----------------------------------------------------------------------------
#  "THE BEER-WARE LICENSE" (Revision 42):
# <hello@reox.at> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return Sebastian Bachmann 
# ----------------------------------------------------------------------------

import numpy
import sys
from math import sqrt, pi, sin, cos, asin, acos
# in mm
r=200.0
# how much slices should be generated
steps = 50.0
# how much of the sphere should be done (from top down)
segment_height=10.0
# anlaufbogenradius
a=10
# we consider that the top of the sphere is X0 Y0 Z0
print "G21 ;mm"
print "G90 ; absolute coordinates"
print "F500 ;500mm/minutes movement speed"
print "M7 ; staubsauger an"
print "S1 M3 ; fraeser einschalten"
print "G4 P2 ; 2 sekunden warten bis motor gut rennt"

print "G0 X0 Y0 Z%f; position ourself above the center of the sphere" %(10)

# going top down
fstart = (pi/2) - 0.01
fstop = asin((r-segment_height) / r)
sys.stderr.write(str(fstart)+" "+str(fstop))

for alpha in numpy.linspace(fstart, fstop, steps):
    p = r * cos(alpha) 
    # need r - ... here to have the circle top on z = 0
    h = (r * sin(alpha)) - r 

    # position vor dem anlaufbogen anfahren
    print "G0 X%f Y%f Z%f" %(-p, -a, h+a)
    # anlaufbogen, ccw in XZ Plane - parallel to Y Axis
    print "G19 G3 Y0 Z%f J%f F100" %(h, a)
    # kreis fraesen
    print "G17 G2 X%f Y0 I%f F100" %(-p, p)

print "G0 X0 Y0 Z%f; position ourself above the center of the sphere" %(40)
print "M30"
