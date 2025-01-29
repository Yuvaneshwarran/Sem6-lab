from collections import deque

def boatride(lm,lc,rm,rc,ch):
    if(lm>=2 and ch==1):
        lm=lm-2
        rm=rm+2
    elif(lc>=2 and ch==2):
        lc=lc-2
        rc=rc+2
    elif(lm>=1 and lc>=2 and ch==3):
        lm=lm-1
        lc=lc-1
        rm=rm+1
        rc=rc+1
    elif(lm>=1 and ch==4):
        lm=lm-1
        rm=rm+1
    elif(lc>=1 and ch==5):
        lc=lc-1
        rc=rc+1
    elif(rm>=2 and ch==6):
        rm=rm-2
        lm=lm+2
    elif(rc>=2 and ch==7):
        rc=rc-2
        rc=rc+2
    elif(rm>=1 and rc>=2 and ch==8):
        rm=rm-1
        rc=rc-1
        lm=lm+1
        lc=lc+1
    elif(rm>=1 and ch==9):
        rm=rm-1
        lm=lm+1
    elif(rc>=1 and ch==10):
        rc=rc-1
        lc=lc+1
    return (lm,lc,rm,rc)

def bfs(m,c):
    open_list=deque([[m,c,0,0]])
    closed_list=set()
    path=''
    while(open_list):
        lm,lc,rm,rc=open_list.popleft()
        path+='->'+str((lm,lc,rm,rc))
        if(lm==0 and lc==0):
            print(lm,lc,rm,rc)
            return path[2:]
        closed_list.add((lm,lc,rm,rc))
        for i in range(1,11):
            node=boatride(lm,lc,rm,rc,i)
            if(node not in closed_list and (((node[0]>=node[1]) or node[0]==0) and ((node[2]>=node[3]) or node[2]==0))):
                open_list.append(node)

def dfs(m,c):
    open_list=deque([[m,c,0,0]])
    closed_list=set()
    path=''
    while(open_list):
        lm,lc,rm,rc=open_list.pop()
        path+='->'+str((lm,lc,rm,rc))
        if(lm==0 and lc==0):
            print(lm,lc,rm,rc)
            return path[2:]
        closed_list.add((lm,lc,rm,rc))
        for i in range(1,11):
            node=boatride(lm,lc,rm,rc,i)
            if(node not in closed_list and (((node[0]>=node[1]) or node[0]==0) and ((node[2]>=node[3]) or node[2]==0))):
                open_list.append(node)

if __name__=='__main__':
    print('BFS path:',bfs(3,3))
    print('DFS path:',dfs(3,3))