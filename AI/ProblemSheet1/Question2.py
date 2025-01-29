import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import random

n=10
G=nx.gnp_random_graph(n,0.4)

for u,v,d in G.edges(data=True):
    d['weight']=random.randint(0,10)    

pos=nx.spring_layout(G)
nx.draw(G,pos,with_labels=True)

edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

plt.show()

start=1
end=3

open_list=[[start,0]]
closed_list=[]


while(open_list):
    minim=9999
    pos=0
    for i in range(len(open_list)):
        if(minim>open_list[i][1]):
            minim=open_list[i][1]
            pos=i
    if(open_list[pos][0]==end):
        print(open_list[pos][0],open_list[pos][1])
        break
    node,cost=open_list[pos]
    closed_list.append(node)
    open_list.remove(open_list[pos])
    print(node,cost)
    for i in G.neighbors(node):
        if(i not in closed_list):
            open_list.append([i,G.get_edge_data(node,i)['weight']+cost])
            