import matplotlib
import matplotlib.pyplot as plt 
import networkx as nx
from breadth_first import calculate_distance 

Karate = nx.read_gml('karate.gml',label='id')
Lesmis = nx.read_gml('lesmis.gml',label='id')
#nx.draw(Karate,with_labels=True)
#plt.show()

kSource=1
kTarget=11
LSource=0
LTarget=46
print("In karate: distance from",kSource,"To",kTarget,"equals",calculate_distance(Karate,kSource,kTarget))
print("In Lesmis: distance from",LSource,"To",LTarget,"equals",calculate_distance(Lesmis,LSource,LTarget))
