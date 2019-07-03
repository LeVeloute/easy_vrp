import matplotlib.pyplot as plt
import time
import os
x = []
y = []
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
for item in vrp1['nodes']:
    x.append(item['posX'])
    y.append(item['posY'])
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
    for item in vrp2['nodes']:
        x.append(item['posX'])
        y.append(item['posY'])
if(os.path.exists("truck2")):
    vrp3 = {}

    vrp3['nodes'] = [{'label': 'depot', 'demand': 0, 'posX': 0, 'posY': 0}]
    file = open("truck2", "r")
    line = file.readline()
    line = file.readline()
    line = file.readline()
    line = file.readline()
    while (line != ""):
        inputs = line.split()
        node = {'label': inputs[0], 'demand': float(inputs[1]), 'posX': float(inputs[2]), 'posY': float(inputs[3])}
        vrp3['nodes'].append(node)
        line = file.readline()

    file.close()
    file = open("truck2Solved", "r")
    line = file.readline()
    tab3 = []
    while (line != ""):
        tab3.append(line.rstrip())
        line = file.readline()
    for item in vrp3['nodes']:
        x.append(item['posX'])
        y.append(item['posY'])

if(os.path.exists("truck3")):
    vrp4 = {}

    vrp4['nodes'] = [{'label': 'depot', 'demand': 0, 'posX': 0, 'posY': 0}]
    file = open("truck3", "r")
    line = file.readline()
    line = file.readline()
    line = file.readline()
    line = file.readline()
    while (line != ""):
        inputs = line.split()
        node = {'label': inputs[0], 'demand': float(inputs[1]), 'posX': float(inputs[2]), 'posY': float(inputs[3])}
        vrp4['nodes'].append(node)
        line = file.readline()

    file.close()
    file = open("truck3Solved", "r")
    line = file.readline()
    tab4 = []
    while (line != ""):
        tab4.append(line.rstrip())
        line = file.readline()
    for item in vrp4['nodes']:
        x.append(item['posX'])
        y.append(item['posY'])

if(os.path.exists("truck4")):
    vrp5 = {}

    vrp5['nodes'] = [{'label': 'depot', 'demand': 0, 'posX': 0, 'posY': 0}]
    file = open("truck4", "r")
    line = file.readline()
    line = file.readline()
    line = file.readline()
    line = file.readline()
    while (line != ""):
        inputs = line.split()
        node = {'label': inputs[0], 'demand': float(inputs[1]), 'posX': float(inputs[2]), 'posY': float(inputs[3])}
        vrp5['nodes'].append(node)
        line = file.readline()

    file.close()
    file = open("truck4Solved", "r")
    line = file.readline()
    tab5 = []
    while (line != ""):
        tab5.append(line.rstrip())
        line = file.readline()
    for item in vrp5['nodes']:
        x.append(item['posX'])
        y.append(item['posY'])

if(os.path.exists("truck5")):
    vrp6 = {}

    vrp6['nodes'] = [{'label': 'depot', 'demand': 0, 'posX': 0, 'posY': 0}]
    file = open("truck5", "r")
    line = file.readline()
    line = file.readline()
    line = file.readline()
    line = file.readline()
    while (line != ""):
        inputs = line.split()
        node = {'label': inputs[0], 'demand': float(inputs[1]), 'posX': float(inputs[2]), 'posY': float(inputs[3])}
        vrp6['nodes'].append(node)
        line = file.readline()

    file.close()
    file = open("truck5Solved", "r")
    line = file.readline()
    tab6 = []
    while (line != ""):
        tab6.append(line.rstrip())
        line = file.readline()
    for item in vrp6['nodes']:
        x.append(item['posX'])
        y.append(item['posY'])

if(os.path.exists("truck6")):
    vrp7 = {}

    vrp7['nodes'] = [{'label': 'depot', 'demand': 0, 'posX': 0, 'posY': 0}]
    file = open("truck6", "r")
    line = file.readline()
    line = file.readline()
    line = file.readline()
    line = file.readline()
    while (line != ""):
        inputs = line.split()
        node = {'label': inputs[0], 'demand': float(inputs[1]), 'posX': float(inputs[2]), 'posY': float(inputs[3])}
        vrp7['nodes'].append(node)
        line = file.readline()

    file.close()
    file = open("truck6Solved", "r")
    line = file.readline()
    tab7 = []
    while (line != ""):
        tab7.append(line.rstrip())
        line = file.readline()
    for item in vrp7['nodes']:
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
previous3 = None
previous4 = None
previous5 = None
previous6 = None
previous7 = None

for loop in range(len(tab1)+10):
    print("aaaa")
    if(previous1 == None):
        plt.pause(0.1)

        for item123 in vrp1['nodes']:
            if(item123['label'] == tab1[loop]):
                plt.plot([0,item123['posX']],[0,item123['posY']],color='green')
                previous1 = item123
    else:
        try:
            for item123 in vrp1['nodes']:
                if(item123['label'] == tab1[loop]):
                    plt.plot([previous1['posX'],item123['posX']],[previous1['posY'],item123['posY']],color='green')
                    previous1 = item123
        except:
            continue
    if(os.path.exists("truck1")):
        plt.pause(0.1)

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
    if (os.path.exists("truck2")):
        plt.pause(0.1)

        if (previous3 == None):
            for item123 in vrp3['nodes']:
                if (item123['label'] == tab3[loop]):
                    plt.plot([0, item123['posX']], [0, item123['posY']], color='blue')
                    previous3 = item123
        else:
            for item123 in vrp3['nodes']:
                try:
                    if (item123['label'] == tab3[loop]):
                        plt.plot([previous3['posX'], item123['posX']], [previous3['posY'], item123['posY']],
                                 color='blue')
                        previous3 = item123
                except:
                    continue
    if (os.path.exists("truck3")):
        plt.pause(0.1)

        if (previous4 == None):
            for item123 in vrp4['nodes']:
                if (item123['label'] == tab4[loop]):
                    plt.plot([0, item123['posX']], [0, item123['posY']], color='pink')
                    previous4 = item123
        else:
            for item123 in vrp4['nodes']:
                try:
                    if (item123['label'] == tab4[loop]):
                        plt.plot([previous4['posX'], item123['posX']], [previous4['posY'], item123['posY']],
                                 color='pink')
                        previous4 = item123
                except:
                    continue
    if (os.path.exists("truck4")):
        plt.pause(0.1)

        if (previous5 == None):
            for item123 in vrp5['nodes']:
                if (item123['label'] == tab5[loop]):
                    plt.plot([0, item123['posX']], [0, item123['posY']], color='orange')
                    previous5 = item123
        else:
            for item123 in vrp5['nodes']:
                try:
                    if (item123['label'] == tab5[loop]):
                        plt.plot([previous5['posX'], item123['posX']], [previous5['posY'], item123['posY']],
                                 color='orange')
                        previous5 = item123
                except:
                    continue
    if (os.path.exists("truck5")):
        plt.pause(0.1)

        if (previous6 == None):
            for item123 in vrp6['nodes']:
                if (item123['label'] == tab6[loop]):
                    plt.plot([0, item123['posX']], [0, item123['posY']], color='yellow')
                    previous6 = item123
        else:
            for item123 in vrp6['nodes']:
                try:
                    if (item123['label'] == tab6[loop]):
                        plt.plot([previous6['posX'], item123['posX']], [previous6['posY'], item123['posY']],
                                 color='yellow')
                        previous6 = item123
                except:
                    continue
    if (os.path.exists("truck6")):
        plt.pause(0.1)

        if (previous7 == None):
            for item123 in vrp7['nodes']:
                if (item123['label'] == tab7[loop]):
                    plt.plot([0, item123['posX']], [0, item123['posY']], color='black')
                    previous7 = item123
        else:
            for item123 in vrp7['nodes']:
                try:
                    if (item123['label'] == tab7[loop]):
                        plt.plot([previous7['posX'], item123['posX']], [previous7['posY'], item123['posY']],
                                 color='black')
                        previous7 = item123
                except:
                    continue


plt.pause(0.0001)
plt.plot([previous1['posX'],0],[previous1['posY'],0],color='green')
plt.plot([previous2['posX'],0],[previous2['posY'],0],color='red')
plt.plot([previous3['posX'],0],[previous2['posY'],0],color='blue')


time.sleep(1000)
