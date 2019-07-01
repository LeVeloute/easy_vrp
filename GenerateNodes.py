# encoding: utf-8
### Un noeud possèdent les caractèrisques suivantes : Coordonnées X, Y


import sys
import random
import math

nodesCount = 0

minNodes = 10
maxNodes = 100
minX = 0
maxX = 100
minY = 0
maxY = 100
minCost = 0
maxCost = 100
file = open("Nodes.txt", "w")

while(nodesCount < minNodes or random.random()>0.05):
    if(nodesCount > maxNodes - 1):
        break
    x = random.uniform(minX, maxX)
    y = random.uniform(minY, maxY)
    file.write(str(nodesCount) + "," + str(x) + "," + str(y) + "\n")
    nodesCount = nodesCount + 1

file.close()
print("Nodes succefuly generated")
