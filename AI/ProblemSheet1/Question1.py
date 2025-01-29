import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def BFS(G,start,end):
    visited=[False]*len(G.nodes())
    queue=deque([[start,[start]]])
    while(len(queue)!=0):
        node,path=queue.popleft()
        if(node==end):
            return path
        #print(node,path)
        visited[node]=True
        for n in G.neighbors(node):
            if(visited[n]==False):
                queue.append([n,path+[n]])
    return []

def DFS(G,start,end):
    visited=[False]*len(G.nodes())
    queue=deque([[start,[start]]])
    while(len(queue)!=0):
        node,path=queue.pop()
        if(node==end):
            return path
        # print(node,path)
        visited[node]=True
        for n in G.neighbors(node):
            if(visited[n]==False):
                queue.append([n,path+[n]])
    return []
    
def DLS(G,start,end,max_depth):
    visited=[False]*len(G.nodes())
    queue=deque([[start,[start],0]])
    while(len(queue)!=0):
        node,path,depth=queue.pop()
        if(node==end):
            return path
        # print(node,path,depth)
        visited[node]=True
        for n in G.neighbors(node):
            if(visited[n]==False and depth<max_depth):
                queue.append([n,path+[n],depth+1])
    return []

def IDS(G,start,end):
    max_depth=0
    for i in range(len(G.nodes())):
            max_depth=max(max_depth,len(DFS(G,start,i)))
    depth=0
    while(depth<=max_depth):
        path_nodes=DLS(G,start,end,depth)
        if path_nodes:
            return path_nodes
        depth+=1
    return []

def plot(G,path_nodes,title='Graph'):
    pos=nx.spring_layout(G)
    nx.draw_networkx(G,pos,with_labels=True)

    if path_nodes:
        edges=list(zip(path_nodes[:-1],path_nodes[1:]))
        nx.draw_networkx_edges(G,pos,edgelist=edges,edge_color='red')

    plt.title(title)
    plt.show()

n=10
G=nx.gnp_random_graph(n,0.4)
nx.draw(G,with_labels=True)
plt.show()

path_nodes=BFS(G,1,3)
print('BFS:',path_nodes)
plot(G,path_nodes,'BFS')

path_nodes=DFS(G,1,3)
print('DFS:',path_nodes)
plot(G,path_nodes,'DFS')

path_nodes=DLS(G,1,3,4)
print('DLS:',path_nodes)
plot(G,path_nodes,'DLS')

path_nodes=IDS(G,1,3)
print('IDS:',path_nodes)
plot(G,path_nodes,'IDS')