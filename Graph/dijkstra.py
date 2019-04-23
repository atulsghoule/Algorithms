from heapq import heappop, heappush
def findShortetPaths(graph, source, size):
    distance = [float('inf')]*size
    visited = [False]* size
    distance[source] = 0
    store = [(0, source)]
    while store:
        dist, parent = heappop(store)
        visited[parent] = True
        for node in graph[parent]:
            if not visited[node] and \
                dist+ graph[parent][node]< distance[node]:
                distance[node] = dist+ graph[parent][node]
                heappush(store, (
                    dist + graph[parent][node],
                    node)
                    )
    return distance

graph = {
    0:{1:2, 2:6, 3:7 },
    1:{0:2, 2:3, 3:1 },
    2:{0:6, 1:3, 3:1 },
    3:{0:7, 1:1, 2:1 }
}
print findShortetPaths(graph, 0, len(graph))