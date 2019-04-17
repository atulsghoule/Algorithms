from sys import stdin,stdout
from bisect import bisect,bisect_left,insort
from math import ceil,floor,log,sqrt
from os import system
system('clear')

def orientation(a,b,c):
    res = (b[1]-a[1]) * (c[0]-b[0]) - (c[1]-b[1]) * (b[0]-a[0])
    if res == 0:
        return 0
    if res >0 :
        return 1
    return -1
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
    # Sorting the points O(N^2) anti-clock wise direction
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
        return brute_hull(hull_points)
    mid = len(hull_points)/2
    sub_hull_1 = divide_hull(list(hull_points[:mid]))
    sub_hull_2 = divide_hull(list(hull_points[mid:]))
    return merge_hull(sub_hull_1,sub_hull_2)
def merge_hull(a,b):
    n1,n2 = len(a),len(b)
    ia,ib = 0,0
    for i in xrange(1,n1):
        if a[i][0] > a[ia][0]:
            ia= i
    inda , indb = ia,ib
    done = False
    while (not done):
        done = 1
        while orientation(b[indb], a[inda], a[(inda+1)%n1]) >=0:
            inda = (inda + 1) % n1
 
        while orientation(a[inda], b[indb], b[(n2+indb-1)%n2]) <=0:
            indb = (n2+indb-1)%n2
            done = 0
    uppera = inda ; upperb = indb
    inda = ia ; indb=ib
    done = 0
    g = 0
    while not done:
        done = 1
        while orientation(a[inda], b[indb], b[(indb+1)%n2])>=0:
            indb=(indb+1)%n2
        while orientation(b[indb], a[inda], a[(n1+inda-1)%n1])<=0:
            inda=(n1+inda-1)%n1
            done=0
    lowera = inda ; lowerb = indb
    ret = list()

    ind = uppera
    ret.append(a[uppera])
    while ind != lowera:
        ind = (ind+1)%n1
        ret.append(a[ind])
    ind = lowerb
    ret.append(b[lowerb])
    while ind != upperb:
        ind = (ind+1)%n2
        ret.append(b[ind])
    return ret

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
print "\n\n\n"
print divide_hull(points)