import numpy as np
import matplotlib.pyplot as plt
import heapq

class solver:
    def __init__(self):
        pass
        
    def hue(self,a,b):
        return np.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

    def astar(self,start,end,grid):
        neighbours=[(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        heap=[]
        closed_list=set()
        gscore={start:0}
        fscore={start:self.hue(start,end)}
        parent={}
        heapq.heappush(heap,(fscore[start],start))
        while heap:
            current=heapq.heappop(heap)[1]
            closed_list.add(current)
            if(current==end):
                data=[]
                while current in parent:
                    data.append(current)
                    current=parent[current]
                return data

            for i,j in neighbours:
                neighbour=current[0]+i,current[1]+j
                tgscore=gscore[current]+self.hue(current,neighbour)
                if 0<=neighbour[0]<grid.shape[0]:
                    if 0<=neighbour[1]<grid.shape[1]:
                        if grid[neighbour[0]][neighbour[1]]:
                            continue
                    else:
                        continue
                else:
                    continue
                if neighbour in closed_list and tgscore>=gscore.get(neighbour,0):
                    continue
                if tgscore<gscore.get(neighbour,0) or neighbour not in [i[1] for i in heap]:
                    parent[neighbour]=current
                    gscore[neighbour]=tgscore
                    fscore[neighbour]=tgscore+self.hue(neighbour,end)
                    heapq.heappush(heap,(fscore[neighbour],neighbour))

        return False
