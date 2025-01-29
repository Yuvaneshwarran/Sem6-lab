from collections import deque

def jugoperations(x,y,ch):
    if(x==0 and ch==1):
        x=4
    elif(y==0 and ch==2):
        y=3
    elif(x>0 and ch==3):
        x=0
    elif(y>0 and ch==4):
        y=0
    elif(x+y>=3 and x>0 and ch==5):
        x=x-(3-y)
        y=3
    elif(x+y>=4 and y>0 and ch==6):
        y=y-(4-x)
        x=4
    elif(x+y<=3 and x>0 and ch==7):
        y=x+y
        x=0
    elif(x+y<=4 and y>0 and ch==8):
        x=x+y
        y=0
    return (x,y)

def bfs(desired,goal_jug):
    open_list=deque([[0,0]])
    closed_list=set()
    path=''
    while(open_list):
        j1,j2=open_list.popleft()
        path+='->'+str((j1,j2))
        if(j1==desired and goal_jug==1) or (j2==desired and goal_jug==2):
            return path[2:]
        closed_list.add((j1,j2))
        for i in range(1,9):
            if(jugoperations(j1,j2,i) not in closed_list):
                open_list.append(jugoperations(j1,j2,i))
    return 'None'

def dfs(desired,goal_jug):
    open_list=deque([[0,0]])
    closed_list=set()
    path=''
    while(open_list):
        j1,j2=open_list.pop()
        path+='->'+str((j1,j2))
        if(j1==desired and goal_jug==1) or (j2==desired and goal_jug==2):
            return path[2:]
        closed_list.add((j1,j2))
        for i in range(1,9):
            if(jugoperations(j1,j2,i) not in closed_list):
                open_list.append(jugoperations(j1,j2,i))
    return 'None'

if __name__ == '__main__':
    print('BFS path:',bfs(3,1))
    print('DFS path:',dfs(3,1))