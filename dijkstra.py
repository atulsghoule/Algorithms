# test Graph
graph = [
    {1:5,4:2,3:9},
    {0:5,2:2},
    {1:2,3:3},
    {2:3,0:9,5:2},
    {0:2,5:3},
    {4:3,3:2}
]
# required functions
def fixHeap(index,size):
    parent = index
    while parent!=0:
        parent/=2
        if minHeap[parent][1] > minHeap[index][1]:
            minHeap[parent],minHeap[index] = minHeap[index],minHeap[parent]
            locationHeap[minHeap[parent][0]],locationHeap[minHeap[index][0]] = parent,index
        else:
            break 
        index = parent
    fixHeapMap(index,size)
def fixHeapMap(index,size):
    c1,c2,pos,ele = 2*index+1,2*index+2,index,minHeap[index][1]
    if c1 < size and minHeap[c1][1] < ele:
        ele,pos = minHeap[c1][1],c1
    if c2 < size and minHeap[c2][1] < ele:
        ele,pos = minHeap[c2][1],c2
    if pos!=index:
        minHeap[index],minHeap[pos] = minHeap[pos],minHeap[index]
        locationHeap[minHeap[pos][0]],locationHeap[minHeap[index][0]] = pos,index
        fixHeapMap(pos,size)
def getMinHeap():
    minHeap[0],minHeap[-1] = minHeap[-1],minHeap[0]
    node = minHeap.pop()
    size,index = len(minHeap),0
    if size != 0:
        locationHeap[node[0]] = float('inf')
        locationHeap[minHeap[0][0]] = 0
        fixHeapMap(index,size)
    return node
# intermediate storage
locationHeap = {i:i for i in xrange(6)}
minHeap = [[i,float('inf')] for i in xrange(6)]
distance = [0]*6
parent = [0]*6
# Dijkstra Algorithm
# source  = 0
minHeap[0][1] = 0

while len(minHeap)!=0:
    node = getMinHeap()
    distance[node[0]] = node[1]
    for key,value in graph[node[0]].iteritems():
        index = locationHeap[key]
        if locationHeap[key] != float('inf') and distance[node[0]] + value < minHeap[index][1]:
            minHeap[index][1] = distance[node[0]] + value
            fixHeap(index,len(minHeap))
            parent[key] = node[0]
print minHeap
print distance
print parent
print locationHeap

