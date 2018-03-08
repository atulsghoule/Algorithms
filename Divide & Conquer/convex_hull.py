from sys import stdin,stdout
from bisect import bisect,bisect_left,insort
from math import ceil,floor,log,sqrt
from os import system
system('clear')


def brute_hull(points):
    hull_points,N=list(),len(points)
    for i in xrange(N):
        for j in xrange(i+1,N):
            #Solving the matrix to obtain sign to know the position
            #   |   x2-x1   x3-x1   |
            #   |   y2-y1   y3-y1   |     
            #------------------------------------------------------
            x1,x2 = points[i][0],points[j][0]
            y1,y2 = points[i][1],points[j][1]
            pos,neg = 0,0
            for k in xrange(N):
                ans = ((x2-x1)*(points[k][1]-y1))-((y2-y1)*(points[k][0]-x1))
                if ans>=0:
                    pos+=1
                if ans<=0:
                    neg+=1
            if neg==N or pos==N:
                hull_points.append(points[i])
                hull_points.append(points[j])
    # Sorting the points O(N^2)
    temp_points,temp_points_index,N =list(),list(),len(hull_points)
    for i in xrange(0,N,2):
        if hull_points[i] in temp_points_index:
            index = temp_points_index.index(hull_points[i])
            if hull_points[i+1] not in temp_points[index]:
                temp_points[index].append(hull_points[i+1])
        else:
            temp_points_index.append(hull_points[i])
            temp_points.append([hull_points[i+1]])
        if hull_points[i+1] in temp_points_index:
            index = temp_points_index.index(hull_points[i+1])
            if hull_points[i] not in temp_points[index]:
                temp_points[index].append(hull_points[i])
        else:
            temp_points_index.append(hull_points[i+1])
            temp_points.append([hull_points[i]])
    
    start,hull_points = temp_points_index[0],[temp_points_index[0]]
    if temp_points[0][0][1]<temp_points[0][1][1]:
        point = temp_points[0][0]
    else:
        point = temp_points[0][1]
    hull_points.append(point)
    while point!= start:
        index = temp_points_index.index(point)
        point = start
        if temp_points[index][0] not in hull_points:
            point = temp_points[index][0]
        elif temp_points[index][1] not in hull_points:
            point = temp_points[index][1]
        hull_points.append(point)
    return hull_points[:-1]
def sorting_points():
    points.sort(key= lambda x:x[0])
def divide_hull(hull_points):
    if len(hull_points)<=5:
        return brure_hull(hull_points)
    mid = len(hull_points)/2
    sub_hull_1 = divide_hull(list(hull_points[:mid]))
    sub_hull_2 = divide_hull(list(hull_points[mid:]))
    return merge_hull(sub_hull_1,sub_hull_2)




def merge_hull(sub_hull_1,sub_hull_2):
    

points  = [
    [-5,5],
    [-3,3],
    [-1,1],
    [-5,1],
    [-6,1],
    
    [3,3],
    [7,2],
    [6,4],

    [5,-2],
    [2,-2],
    [3,-3],
    [4,-5],

    [-2,-2],
    [-2,-4]
]
sorting_points()
print brute_hull(points)