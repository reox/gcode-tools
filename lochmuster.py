startx = -150
starty = -80

deltax = 20
deltay = 20

repx = 300/deltax
repy = 160/deltay

xaxis = map(lambda x: startx+deltax*x, range(repx+1))
yaxis = map(lambda x: starty+deltay*x, range(repy+1))

for y in yaxis:
    for x in xaxis:
        print "G0 X%d Y%d" %(x,y)
        print "G0 Z1"
        print "G83 Z-4 R1 Q0.5"
        print "G0 Z10"
    xaxis.reverse() 

