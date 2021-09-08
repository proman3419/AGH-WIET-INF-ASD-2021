from zad3testy import runtests
from queue import PriorityQueue
from math import inf


# O(V + (V^3)*log(V))
def dijkstra_am_pq(graph, s, w):
  n = len(graph)
  queue = PriorityQueue()
  visited = [[False for _ in range(3)] for _ in range(n)]
  distances = [[inf for _ in range(3)] for _ in range(n)]

  distances[s][0] = 0
  # druga wartosc w krotce oznacza typ wierzcholka:
  # 0 - mozna uzyc butow
  # 1 - uzyto butow na poprzednim wierzcholku, obecny jest pomijany
  queue.put((distances[s], 0, s))

  while not queue.empty():
    dist, _type, u  = queue.get()

    if not visited[u][_type]:
      visited[u][_type] = True

      for v in range(n):
        if graph[u][v] > 0:
          new_dist = distances[u][_type] + graph[u][v]
          if distances[v][0] > new_dist:
            visited[v][0] = False
            distances[v][0] = new_dist
            queue.put((distances[v][0], 0, v))

          if _type == 0:
            # uzywamy butow u -> (v) -> t
            for t in range(n):
              new_dist = distances[u][0] + max(graph[u][v], graph[v][t])
              if graph[v][t] > 0:
                if distances[t][1] > new_dist:
                  visited[t][1] = False
                  distances[t][1] = new_dist
                  queue.put((distances[t][1], 1, t))

  return min(distances[w])


def jumper(G, s, w):
  return dijkstra_am_pq(G, s, w)


runtests(jumper)
