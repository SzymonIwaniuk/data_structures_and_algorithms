from egz2Atesty import runtests


def build_graph(V, E):
  graph = [[] for _ in range(V)]

  for a, b in E:
    graph[a].append(b)
    graph[b].append(a)

  return graph


def kingnqueen( V,E,D,K,Q,B ):
  # tu prosze wpisac wlasna implementacje
  graph = build_graph(V, E)

  tin = [-1] * V
  tout = [-1] * V
  low = [0] * V
  parent = [-1] * V
  time = 0

  art = [[] for _ in range(V)]

  def dfs(u):
    nonlocal time
    time += 1
    tin[u] = low[u] = time
    child_cnt = 0
    for v in graph[u]:
      if tin[v] == -1:
        parent[v] = u
        child_cnt += 1

        dfs(v)
        low[u] = min(low[u], low[v])
        if parent[u] != -1 and low[v] >= tin[u]:
          art[u].append(v)
      elif v != parent[u]:
        low[u] = min(low[u], tin[v])
    if parent[u] == -1 and child_cnt >= 2:
      art[u] = G[u][:]
    time += 1
    tout[u] = time

  dfs(0)

  def same_subtree(k, q, b):
    def subtree(v):
      for c in art[b]:
        if tin[c] <= tin[v] <= tout[c]:
          return c
      return -1

    return subtree(k) == subtree(q)

  res = 0
  for d in range(D):
    k, q, b = K[d], Q[d], B[d]
    if len(art[b]) == 0:
      res += 1
    elif same_subtree(k, q, b):
      res += 1

  return res
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kingnqueen, all_tests = True )
