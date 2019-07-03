import os


y = 0
while(os.path.exists("truck" + str(y) + "Solved")):
    print("delete")
    os.remove("truck" + str(y) + "Solved")
    y = y + 1

y = 0
while(os.path.exists("truck" + str(y))):
    y = y + 1

for loop in range(y):
    os.system("C:/Python27/python.exe GeneticEngineV2.py 50 100 truck" + str(loop) +" < truck" + str(loop))

#os.system("C:/Python27/python.exe TestGenerateSimulation.py")