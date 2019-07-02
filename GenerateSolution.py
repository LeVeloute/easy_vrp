import os


y = 0
while(os.path.exists("truck" + str(y) + "Solved")):
    print("delete")
    os.remove("truck" + str(y) + "Solved")
    y = y + 1

os.system("C:/Python27/python.exe GenerateSolution.py 50 100 truck0 < truck0")