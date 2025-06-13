def hungry_frog(S):
    # f(i) minimalna liczba skokow do dotarcia do indeksu i

    # Tworzymy macierz skokow i ilosci energi jak w bfs z throtlingiem np - dp
    # f(i,j)
    # min(f(i - l, j - S[i] - l) 1)
    #    l <= j - S[i]
    # Zjadanie najwiekszego jedzenia w "oknie" aktualnej ilosci energi
    pass
