import argparse
from math import sqrt, acos, pi, atan2, cos, sin, hypot

def dotproduct(v1, v2):
    return sum((a*b) for a, b in zip(v1, v2))

def angle(v1, v2):
    return acos(dotproduct(v1, v2) / (hypot(v1[0], v1[1]) * hypot(v2[0], v2[1])))

def main():
    parser = argparse.ArgumentParser(description="Calculate G10 Rotation Command by giving two points of the workpiece.\nMachine Coordinates of main point (P1) can be specified, if P1 is not (0,0). Then a translation will also be calculated.") 
    parser.add_argument('-p1', type=float, nargs=2, help='first point', dest='p1', required=True)
    parser.add_argument('-p2', type=float, nargs=2, help='second point', dest='p2', required=True)

    parser.add_argument('-m', type=float, nargs=2, help='machine coordinates of point p1', dest='m')

    args = parser.parse_args()
    
    x1, y1 = args.p1
    x2, y2 = args.p2
    xm, ym = args.m
    
    # vector from p1 to p2
    vp = [x2-x1, y2-y1]
    # vector from zero point to p1
    vn = [x1, y1]

    # angle between x axis and vector p1 -> p2
    alpha = atan2(vp[1], vp[0])

    if vn != [0,0]:
        # if our p1 is not the zero point, we need to translate too
        # angle between vn and x axis
        beta = angle(vp, vn) - alpha

        l_vn = hypot(x1,y1)
        # distance between zero point and p1 on x/y axis
        d_x = l_vn * cos(beta)
        d_y = l_vn * sin(beta)

        # calculate zero point offset based on machine coordinates
        dm_x = xm - d_x
        dm_y = ym - d_y

        print "G10 L2 P1 X%f Y%f R%f" %(dm_x, dm_y, alpha/pi*180)
    else:
        print "G10 L2 P1 R%f" %alpha


if __name__ == '__main__':
    main()
