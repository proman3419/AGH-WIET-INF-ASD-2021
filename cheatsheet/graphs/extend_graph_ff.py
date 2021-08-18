# do dodawania super zrodla (SZ) i super ujscia (SU), wykorzystywane w fordzie-fulkersonie


def extend_graph_ff(graph, srcs, sinks):
  n = len(graph)

  graph.append([0]*n) # SZ
  graph.append([0]*n) # SU

  n = len(graph)

  srcs.sort()
  sinks.sort()
  i = j = 0

  for k in range(n):
    graph[k].append(0)
    graph[k].append(0)

    if i < len(srcs) and k == srcs[i]:
      graph[-2][k] = inf # SZ
      i += 1

    if j < len(sinks) and k == sinks[j]:
      graph[k][-1] = inf # SU
      j += 1

  return graph
