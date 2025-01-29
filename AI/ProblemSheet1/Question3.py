import numpy as np

def h(puzzle):
    heuristic=0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if(puzzle[i][j]==goal[i][j]):
                heuristic=heuristic+1
            else:
                heuristic=heuristic-1
    return heuristic

def pos(state):
    for i in range(len(state)):
        for j in range(len(state[0])):
            if(state[i][j]==0):
                return i,j

def moves(state):
    temp=state.copy()
    i,j=pos(state)
    successor_states=[]
    if(i+1<len(state)):
        state[i][j],state[i+1][j]=state[i+1][j],state[i][j]
        successor_states.append(state)
        state=temp.copy()
    if(i-1>=0):
        state[i][j],state[i-1][j]=state[i-1][j],state[i][j]
        successor_states.append(state)
        state=temp.copy()
    if(j+1<len(state[0])):
        state[i][j],state[i][j+1]=state[i][j+1],state[i][j]
        successor_states.append(state)
        state=temp.copy()
    if(j-1>=0):
        state[i][j],state[i][j-1]=state[i][j-1],state[i][j]
        successor_states.append(state)
    return successor_states

def hillclimbing(state):
    current_h=h(state)
    current_state=state.copy()
    for s in moves(state.copy()):
        if(current_h<h(s)):
            current_h=h
            current_state=s.copy()
    if((current_state==state).all()):
        print('Optimum:',current_state)
        print('Heuristic:',current_h)
    else:
        print(current_state)
        hillclimbing(current_state.copy())


# start=np.array([[7,2,4],[5,0,6],[8,3,1]])
start=np.array([[8,4,7],[2,6,3],[5,1,0]])
goal=np.array([[0,1,2],[3,4,5],[6,7,8]])
hillclimbing(start)