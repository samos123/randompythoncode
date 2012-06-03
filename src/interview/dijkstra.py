import sys

def shortestpath(graph,start,end,visited=[],distances={},predecessors={}):
    """Find the shortest path between start and end nodes in a graph"""
    # we've found our end node, now find the path to it, and return
    if start==end:
        path=[]
        while end != None:
            path.append(end)
            end=predecessors.get(end,None)
        return distances[start], path[::-1]
    # detect if it's the first time through, set current distance to zero
    if not visited: distances[start]=0
    # process neighbors as per algorithm, keep track of predecessors
    for neighbor in graph[start]:
        if neighbor not in visited:
            neighbordist = distances.get(neighbor,sys.maxint)
            tentativedist = distances[start] + graph[start][neighbor]
            if tentativedist < neighbordist:
                distances[neighbor] = tentativedist
                predecessors[neighbor]=start
    # neighbors processed, now mark the current node as visited
    visited.append(start)
    # finds the closest unvisited node to the start
    unvisiteds = dict((k, distances.get(k,sys.maxint)) for k in graph if k not in visited)
    closestnode = min(unvisiteds, key=unvisiteds.get)
    # now we can take the closest node and recurse, making it current
    return shortestpath(graph, closestnode, end, visited, distances, predecessors)



if __name__ == "__main__":
    graph = {'a': {'w': 14, 'x': 7, 'y': 9},
            'b': {'w': 9, 'z': 6},
            'w': {'a': 14, 'b': 9, 'y': 2},
            'x': {'a': 7, 'y': 10, 'z': 15},
            'y': {'a': 9, 'w': 2, 'x': 10, 'z': 11},
            'z': {'b': 6, 'x': 15, 'y': 11}}
#    graph = {'x7_y8': {'x6_y6': 1}, 'x7_y9': {'x5_y8': 1}, 'x7_y1': {'x6_y3': 1}, 'x7_y2': {'x5_y1': 1}, 'x7_y3': {'x6_y1': 1}, 'x7_y4': {'x5_y3': 1}, 'x7_y5': {'x6_y3': 1}, 'x7_y6': {'x6_y4': 1}, 'x7_y7': {'x6_y5': 1}, 'x5_y8': {'x3_y7': 1}, 'x5_y9': {'x4_y7': 1}, 'x5_y6': {'x4_y4': 1}, 'x5_y7': {'x4_y5': 1}, 'x6_y5': {'x5_y3': 1}, 'x5_y5': {'x4_y3': 1}, 'x5_y2': {'x4_y4': 1}, 'x5_y3': {'x3_y2': 1}, 'x6_y1': {'x5_y3': 1}, 'x5_y1': {'x3_y2': 1}, 'x4_y10': {'x2_y9': 1}, 'x6_y9': {'x5_y7': 1}, 'x6_y8': {'x5_y6': 1}, 'x2_y10': {'x1_y8': 1}, 'x3_y8': {'x2_y6': 1}, 'x3_y9': {'x2_y7': 1}, 'x3_y4': {'x1_y3': 1}, 'x3_y5': {'x2_y3': 1}, 'x3_y6': {'x2_y4': 1}, 'x3_y7': {'x1_y6': 1}, 'x3_y1': {'x2_y3': 1}, 'x3_y2': {'horse': 1}, 'x3_y3': {'x1_y2': 1}, 'x4_y9': {'x3_y7': 1}, 'x4_y8': {'x3_y6': 1}, 'x4_y5': {'x2_y4': 1}, 'x4_y4': {'x3_y2': 1}, 'x4_y7': {'x3_y5': 1}, 'x4_y6': {'x3_y4': 1}, 'x4_y1': {'x5_y3': 1}, 'x4_y3': {'x2_y4': 1}, 'x4_y2': {'x2_y3': 1}, 'x2_y9': {'x3_y7': 1}, 'x2_y8': {'x1_y6': 1}, 'x9_y10': {'x7_y9': 1}, 'x10_y9': {'x9_y7': 1}, 'x10_y8': {'x8_y7': 1}, 'x2_y3': {'horse': 1}, 'x2_y2': {'x4_y3': 1}, 'x10_y5': {'x9_y3': 1}, 'x10_y4': {'x8_y3': 1}, 'x10_y3': {'x9_y1': 1}, 'x2_y6': {'x4_y5': 1}, 'x10_y1': {'x9_y3': 1}, 'x2_y4': {'x3_y2': 1}, 'x8_y10': {'x7_y8': 1}, 'x1_y10': {'x2_y8': 1}, 'x7_y10': {'x6_y8': 1}, 'x8_y9': {'x7_y7': 1}, 'x8_y8': {'x7_y6': 1}, 'horse': 0, 'x8_y1': {'x6_y2': 1}, 'x8_y3': {'x6_y2': 1}, 'x8_y2': {'x6_y3': 1}, 'x8_y5': {'x6_y4': 1}, 'x8_y4': {'x7_y2': 1}, 'x8_y7': {'x6_y6': 1}, 'x8_y6': {'x7_y4': 1}, 'x1_y8': {'x3_y7': 1}, 'x1_y9': {'x2_y7': 1}, 'x1_y2': {'x2_y4': 1}, 'x1_y3': {'x3_y2': 1}, 'x1_y6': {'x2_y4': 1}, 'x1_y7': {'x3_y6': 1}, 'x1_y4': {'x3_y5': 1}, 'x1_y5': {'x2_y3': 1}, 'x5_y10': {'x4_y8': 1}, 'x10_y2': {'x8_y1': 1}, 'x10_y10': {'x9_y8': 1}, 'x10_y7': {'x9_y5': 1}, 'x10_y6': {'x8_y5': 1}, 'x2_y1': {'x1_y3': 1}, 'x2_y7': {'x1_y5': 1}, 'x6_y10': {'x5_y8': 1}, 'x2_y5': {'x1_y3': 1}, 'x3_y10': {'x2_y8': 1}, 'x9_y2': {'x8_y4': 1}, 'x9_y3': {'x7_y2': 1}, 'x9_y1': {'x7_y2': 1}, 'x9_y6': {'x8_y4': 1}, 'x9_y7': {'x8_y5': 1}, 'x9_y4': {'x8_y2': 1}, 'x9_y5': {'x7_y4': 1}, 'x9_y8': {'x8_y6': 1}, 'x9_y9': {'x8_y7': 1}, 'x6_y7': {'x5_y5': 1}, 'x6_y6': {'x4_y5': 1}, 'x5_y4': {'x4_y2': 1}, 'x6_y4': {'x4_y3': 1}, 'x6_y3': {'x5_y1': 1}, 'x6_y2': {'x4_y3': 1}}

    
    
    
    print shortestpath(graph,'b','w')