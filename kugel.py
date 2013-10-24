import numpy
from math import sqrt
# in mm
radius=200

segment_height=10
a_p = 0.5
a=1
# we consider that the top of the sphere is X0 Y0 Z0
print "G21 ;mm"
print "G90 ; absolute coordinates"
print "F500 ;500mm/minutes movement speed"
print "M7 ; staubsauger an"
print "S1 M3 ; fraeser einschalten"
print "G4 P2 ; 2 sekunden warten bis motor gut rennt"

print "G0 X0 Y0 Z%f; position ourself above the center of the sphere" %(10)

basic = False

for z in numpy.arange(start=radius-segment_height, stop=radius, step=a_p)[::-1]:
    # radius at height h = radius * cos(arcsin(z/radius)) = sqrt(radius**2 - z**2) 
    p = sqrt(radius**2 - z**2) 
    h = z - radius

    if basic:
        # punkt am radius anfahren
        print "G0 X%f Y0 Z%f" %(-p, h)
        
        # einen kreis fahren
        print "G2 X%f Y0 I%f F200" %(-p, p)

    else:
        # position vor dem anlaufbogen anfahren
        print "G0 X%f Y%f Z%f" %(-p, -a, h+a)
        # anlaufbogen, ccw in XZ Plane - parallel to Y Axis
        print "G19 G3 Y0 Z%f J%f F100" %(h, a)
        # kreis fraesen
        print "G17 G2 X%f Y0 I%f F100" %(-p, p)

print "G0 X0 Y0 Z%f; position ourself above the center of the sphere" %(radius+40)
print "M30"
