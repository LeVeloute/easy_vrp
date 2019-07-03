import matplotlib.pyplot as plt
import time
import os

### CAMION 1
vrp1 = {}

vrp1['nodes'] = [{'label' : 'depot', 'demand' : 0, 'posX' : 0, 'posY' : 0}]
file = open("truck0", "r")
line = file.readline()
line = file.readline()
line = file.readline()
line = file.readline()
while(line != ""):
    inputs = line.split()
    node = {'label': inputs[0], 'demand': float(inputs[1]), 'posX': float(inputs[2]), 'posY': float(inputs[3])}
    vrp1['nodes'].append(node)
    line = file.readline()

file.close()
file = open("truck0Solved","r")
line = file.readline()
tab1 = []
while(line != ""):
    tab1.append(line.rstrip())
    line = file.readline()

### CAMION 2

if(os.path.exists("truck1")):
    vrp2 = {}

    vrp2['nodes'] = [{'label': 'depot', 'demand': 0, 'posX': 0, 'posY': 0}]
    file = open("truck1", "r")
    line = file.readline()
    line = file.readline()
    line = file.readline()
    line = file.readline()
    while (line != ""):
        inputs = line.split()
        node = {'label': inputs[0], 'demand': float(inputs[1]), 'posX': float(inputs[2]), 'posY': float(inputs[3])}
        vrp2['nodes'].append(node)
        line = file.readline()

    file.close()
    file = open("truck1Solved", "r")
    line = file.readline()
    tab2 = []
    while (line != ""):
        tab2.append(line.rstrip())
        line = file.readline()





x = []
y = []

for item in vrp1['nodes']:
    x.append(item['posX'])
    y.append(item['posY'])
for item in vrp2['nodes']:
    x.append(item['posX'])
    y.append(item['posY'])

plt.scatter(x,y)
plt.title('Simulation VRP')
plt.xlabel('x')
plt.ylabel('y')
print("aaaa")
plt.ion()
plt.draw()
print("aaaa")

previous1 = None
previous2 = None
for loop in range(len(tab1)):
    plt.pause(0.1)
    print("aaaa")
    if(previous1 == None):
        for item123 in vrp1['nodes']:
            if(item123['label'] == tab1[loop]):
                plt.plot([0,item123['posX']],[0,item123['posY']],color='green')
                previous1 = item123
    else:
        for item123 in vrp1['nodes']:
            if(item123['label'] == tab1[loop]):
                plt.plot([previous1['posX'],item123['posX']],[previous1['posY'],item123['posY']],color='green')
                previous1 = item123

    if(previous2 == None):
        for item123 in vrp2['nodes']:
            if(item123['label'] == tab2[loop]):
                plt.plot([0,item123['posX']],[0,item123['posY']],color='red')
                previous2 = item123
    else:
        for item123 in vrp2['nodes']:
            try:
                if(item123['label'] == tab2[loop]):
                    plt.plot([previous2['posX'],item123['posX']],[previous2['posY'],item123['posY']],color='red')
                    previous2 = item123
            except:
                continue


plt.pause(0.0001)
plt.plot([previous1['posX'],0],[previous1['posY'],0],color='green')
plt.plot([previous2['posX'],0],[previous2['posY'],0],color='red')


time.sleep(1000)
