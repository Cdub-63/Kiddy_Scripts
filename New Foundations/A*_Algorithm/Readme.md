A* is an optimized version of Dijkstra’s algorithm. While Dijkstra’s algorithm is concerned with find the shortest distance from one vertex to every other vertex. A* is on concerned with finding the most optimal path to a target vertex. 

Think "I want to find the shortest path from NYC to LA" instead of "I want to know the shortest path from every US city to every other US city"

To implement A*, you can first start with Dijkstra’s algorithm. This is our beginning:
```py
from math import inf
from heapq import heappop, heappush

def a_star(graph, start):
  distances = {}
  for vertex in graph:
    distances[vertex] = inf
  
  distances[start] = 0
  vertices_to_explore = [(0, start)]

  while vertices_to_explore:
    current_distance, current_vertex = heappop(vertices_to_explore)
    for neighbor, edge_weight in graph[current_vertex]:
      new_distance = current_distance + edge_weight
      if new_distance < distances[neighbor]:
        distances[neighbor] = new_distance
        heappush(vertices_to_explore, (new_distance, neighbor))
  
  return distances
```

There are only a few important changes you will need to make:
 - Include a target for the search to find. No more searching in all directions for all destinations.
 - Collect and return the shortest path. A dictionary of distances is cool and all, but A* is on a mission to get you to your target destination and tell you how to get there.
 - Build a heuristic that calculates the estimated distance between two points. This is the crucial point of difference between Dijkstra’s and A*; A* has a real sense of direction.
"""

