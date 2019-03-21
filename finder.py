import cv2
import numpy as np
from grid import gridmaker
import matplotlib.pyplot as plt
from pathsolver import solver
obj=gridmaker(20)
solve=solver()


def line(route):
    xc=[]
    yc=[]
    for i in (range(0,len(route))):
        x=route[i][0]
        y=route[i][1]
        xc.append(x)
        yc.append(y)
    return xc,yc


cap=cv2.VideoCapture(1)
while 1:
    ret,frame=cap.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    th,frame=cv2.threshold(frame,100,255,cv2.THRESH_BINARY)
    frame=cv2.bitwise_not(frame)
    frame=cv2.dilate(frame,None,iterations=5)
    cv2.imshow("frame",frame)
    if(cv2.waitKey(1) & 0XFF==ord('q')):
        cv2.imwrite("frame.jpg",frame)
        break
cap.release()
cv2.destroyAllWindows()

def main():
    global obj,solve
    fig,ax=plt.subplots()
    grid=obj.returnGrid()
    ax.imshow(grid,cmap=plt.cm.Spectral)
    plt.show()
    print("enter start point")
    s1=int(input())
    s2=int(input())
    start=(s1,s2)
    print("enter end point")
    s1=int(input())
    s2=int(input())
    end=(s1,s2)
    route=solve.astar(start,end,grid)
    if(route==False):
        print("No path")
        return 0
    route+=[start]
    route=route[::-1]

    xc,yc=line(route)
    fig,ax=plt.subplots()
    ax.imshow(grid,cmap=plt.cm.Spectral)
    ax.plot(yc,xc,color="black")
    ax.scatter(start[1],start[0])
    ax.scatter(end[1],end[0])
    plt.show()
if(__name__=="__main__"):
    main()
