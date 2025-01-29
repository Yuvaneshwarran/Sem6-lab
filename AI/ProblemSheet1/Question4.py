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

def h(jug):
    return abs(jug[0]-2)

def hillclimbing(jug):
    if(jug[0]==2):
        print(jug)
        return
    
    current_h=h(jug)
    current_jug=jug
    for i in range(1,9):
        j=jugoperations(jug[0],jug[1],i)
        if(h(j)<current_h):
            current_h=h(j)
            current_jug=j
    if(current_jug==jug):
        print(jug)
        return
    else:
        print(current_jug,'->',end='')
        hillclimbing(current_jug)

if __name__ == '__main__':
    print('(0,0)->',end='')
    hillclimbing((0,0))
 