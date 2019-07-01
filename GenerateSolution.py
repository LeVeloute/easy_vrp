import networkx as nx
import matplotlib.pyplot as plt

file = open("Nodes.txt", "r")
Graph = nx.Graph()

for line in file:
    data = line.rstrip().split(',')
    print(data)
    print(data[1])
    Graph.add_node(data[0],pos=(data[2],data[1]))

pos=nx.get_node_attributes(Graph,'pos')
print(pos)

nx.draw(Graph,pos)
plt.show()