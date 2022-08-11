import networkx as nx 
import os, re
import pygraphviz as pgv 
import random
 

G=nx.Graph(pgv.AGraph('UArizona_Collaboration_Network.dot'))
print(nx.info(G))
nx.write_gpickle(G, "UArizona_Collaboration_Network.gpickle")
 