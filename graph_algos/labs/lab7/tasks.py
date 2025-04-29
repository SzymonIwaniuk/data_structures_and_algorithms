# 1. Transport atomowy
# Dwoch technikow nie moze sie zblizyc na okreslona odleglosc d i jeden startuje z s->t drugi t->s
# w jednym kroku rusza sie jeden albo obaj A wedruje z s->t B wedruje z t->s
# O(V^4) zlozonosc akceptowalna
# O(V^3) zlozonosc wzorcowa
# floyd warshall dzieki czemu mam odleglosci miedzy kazdym wierzcholkiem
# pary pozycji technika a i b ktory ma wieksze odleglosci dla kazdej pary sprawdzamy czy je mozna polaczyc
# Nastepnie bfs sprawdzamy czy jest sciezka z s do t

# 2. Arbitraz Mamy waluty o nr od 1 do n
#K[x][y] = ile waluty y dostaje za x
#Czy istnieje seria tranzakcji gdzie za jednostke pewnej waluty dostaje jej wiecej niz jeden
# Inizjalizacja grafu: budujemy graf gdzie krawedz pomiedzy walutami to logarytm z 1 przez wartosc

# 3. Najkrotsze sciezki przy malejacych krawedziach

# 4. Domkniecie przechodnie grafu G skierowanego to taki graf G' ze jesli G ma sciezke z u do v to G' ma krawedz z u do v
# Checemy algorytm obliczajacy domkniecie przechodnie rep macierzowa
# algorytm floyda - warshalla
# dostajemy macierz incydencji i robimy graf jol


# 5 Algorytm kruskala

