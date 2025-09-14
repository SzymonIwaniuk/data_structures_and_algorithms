from egz3Atesty import runtests

"""
Autor rozwiazania: Szymon Iwaniuk
Opis: Moje rozwiazanie polega na za zachlannym przechodzeniu po kolejnych drzewach i sprawdzaniu czy
poprzedznie drzewa z wraz z aktualnym tworza pare taka ze i < j i H[i] > H[j] jezeli tak aktualizuje tmp jezeli tmp
przekroczy k zwracam result jezeli nie to aktualizuje result o 1. Na koncu zwracam result. Zlozonosc algorytmu oceniam
na O(n^2)
"""

def treecut( H, k ):
  # tu prosze wpisac wlasna implementacje
  n = len(H)
  res = 1
  tmp = 0

  for i in range(1, n):
    for j in range(i-1, -1, -1):
      if H[j] > H[i]:
        tmp += 1

      if tmp > k:
        return res

    res += 1

  return res



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( treecut, all_tests = True)
