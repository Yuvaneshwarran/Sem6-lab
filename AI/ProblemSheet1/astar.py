import networkx as nx
import matplotlib.pyplot as plt
import heapq

def plot(G,path_nodes,title='Graph'):
    pos=nx.spring_layout(G)
    nx.draw_networkx(G,pos,with_labels=True)

    if path_nodes:
        edges=list(zip(path_nodes[:-1],path_nodes[1:]))
        nx.draw_networkx_edges(G,pos,edgelist=edges,edge_color='red')

    plt.title(title)
    plt.show()


G=nx.DiGraph()

G.add_weighted_edges_from([('S','A',4),('S','B',10),('S','C',11),
('A','B',8),('A','D',5),('B','D',15),
('C','D',8),('C','E',20),('C','F',2),
('D','H',16),('D','I',20),('D','F',1),
('E','G',19),('F','G',13),('H','I',1),
('H','J',2),('I','J',5),('I','K',13),
('I','G',5),('J','K',7),('K','G',16)])

heuristic={'S':7,'A':8,'B':6,'C':5,'D':5,'E':3,'F':3,
           'G':0,'H':7,'I':4,'J':5,'K':3}

pos=nx.spring_layout(G)
nx.draw(G,pos,with_labels=True)

edge_labels=nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos,edge_labels)
plt.show()

start='S'
goal='G'
prev='S'
open_list=[[0,start,[start]]]
closed_list=[]
path_cost=0
while(open_list):
    heapq.heapify(open_list)
    cost,node,path=heapq.heappop(open_list)
    closed_list.append(node)
    if(node!=start):
        path_cost+=G[prev][node]['weight']
        prev=node
    if node==goal:
        print('Shortest path:',path)
        print('Cost:',path_cost)
        plot(G,path,'A* Algorithm')
        break
    open_list=[]
    for n in G[node]:
        if n not in closed_list:
            open_list.append([G[node][n]['weight']+heuristic[n],n,path+[n]])
    