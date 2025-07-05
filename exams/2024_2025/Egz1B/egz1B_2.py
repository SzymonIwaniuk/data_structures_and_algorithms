from egz1Btesty import runtests

"""
Szymon Iwaniuk
Moje rozwiazanie opiera sie na tym, iz z tresci zadania wynika ze jest to DAG, wiec buduje i sortuje graf
topologicznie, a nastepnie od tylu sprawdzam czy istnieja mosty w aktualnym potgrafie od wierzcholka i,
jezeli tak to uzupelniam slownik na mosty i update'tuje licznik na koncu zwracam liczbe mostow.
Zlozonosc rozwiazania szacuje na czyli O(EV + V^2).
"""


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(critical, all_tests=True)
