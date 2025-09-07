from egz2Atesty import runtests
from collections import deque
"""
Autor rozwiazania: Szymon Iwaniuk
Na poczatku buduje listowa reprezentacje grafu z listy krawedzi E, nastepnie wywoluje D razy bfs'a
sprawdzajac czy w danym dniu jest mozliwe wyslanie kuriera z wiadomoscia do krolowej dotyczaca ich
ulubionego kota Szrediego, omijajac miasto w ktorym szpiedzy Bajtocji prowadza akcje dywersyjna, w
visited jest oznaczone ono jako None. Jezeli jest to mozliwe to zwracam True i aktualizuje res o 1.
Na koncu zwracam result. Zlozonosc algorytmu oceniam na O(D(V + E)) ponieaz D razy wywoluje bfs (V + E)
"""


def build_graph(V, E):
  graph = [[] for _ in range(V)]

  for a, b in E:
    graph[a].append(b)
    graph[b].append(a)

  return graph


def bfs(queen, king, dyw, graph, V):
  visited = [False for _ in range(V)]
  visited[king] = True
  visited[dyw] = None
  queue = deque()
  queue.append(king)

  while queue:
    city = queue.popleft()

    for next_city in graph[city]:
      if next_city == queen:
        return True

      if visited[next_city] == False:
        visited[next_city] = True
        queue.append(next_city)

  return False


def kingnqueen( V,E,D,K,Q,B ):
  # tu prosze wpisac wlasna implementacje
  graph = build_graph(V, E)
  res = 0

  for i in range(D):
    queen = Q[i]
    king = K[i]
    dyw = B[i]
    if bfs(queen, king, dyw, graph, V):
      res += 1

  return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kingnqueen, all_tests = True )
