import matplotlib.pyplot as plt

vrp = {}

vrp['nodes'] = [{'label' : 'depot', 'demand' : 0, 'posX' : 0, 'posY' : 0}]
file = open("truck0", "r")
line = file.readline()
line = file.readline()
line = file.readline()
line = file.readline()
while(line != ""):
    inputs = line.split()
    node = {'label': inputs[0], 'demand': float(inputs[1]), 'posX': float(inputs[2]), 'posY': float(inputs[3])}
    vrp['nodes'].append(node)
    line = file.readline()



x = []
y = []

for item in vrp['nodes']:
    x.append(item['posX'])
    y.append(item['posY'])



plt.scatter(x,y)
plt.plot(x,y)

plt.title('Simulation VRP')
plt.xlabel('x')
plt.ylabel('y')

plt.show()