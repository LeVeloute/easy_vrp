import os
import time
import csv

pop = 50
iteration = 100

currentTime = time.time()

y = 0
while(os.path.exists("truck" + str(y) + "Solved")):
    print("delete")
    os.remove("truck" + str(y) + "Solved")
    y = y + 1

y = 0
while(os.path.exists("truck" + str(y))):
    y = y + 1

for loop in range(y):
    os.system("python GeneticEngine.py " + str(pop) + " " + str(iteration) + " truck" + str(loop) +" < truck" + str(loop))

duration = (time.time()) - currentTime
print("Duration time: " + str(duration))