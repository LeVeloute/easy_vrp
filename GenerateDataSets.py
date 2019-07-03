# encoding: utf-8


import sys
import random
import math
import os
import sys

y = 0
while(os.path.exists("truck" + str(y))):
    print("delete")
    os.remove("truck" + str(y))
    y = y + 1

y = 0
while(os.path.exists("truck" + str(y) + "Solved")):
    print("delete")
    os.remove("truck" + str(y) + "Solved")
    y = y + 1


maxcap = 10
minX = -100
maxX = 100
minY = -100
maxY = 100
nodesCount = int(sys.argv[1])


o = 0
while(o < 1):
    print("Their is a colis")
    truck = "truck" + str(o)
    file = open(truck, "w")

    file.write('params:')
    file.write('\n')
    file.write('  capacity %f' % maxcap)
    file.write('\n')
    file.write('nodes:')
    file.write('\n')

    i = 0
    while(i < nodesCount):

        demand = random.uniform(0.00001, maxcap)
        x = random.uniform(minX, maxX)
        y = random.uniform(minY, maxY)
        file.write(str('  node%0' + str(math.ceil(math.log(nodesCount + 1) / math.log(10))) + 'd\t\t%.3f\t\t%.3f\t\t%.3f') % (i+1, demand, x, y))
        file.write('\n')
        i = i + 1

    file.close()
    o=o+1
print("Nodes succefuly generated")
