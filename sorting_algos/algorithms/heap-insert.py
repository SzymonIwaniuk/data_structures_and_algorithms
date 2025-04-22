def heap_insert(T, value):
    T.append(value)
    i = len(T) - 1

    while i > 0 and T[parent(i)] < T[i]:
        T[parent(i)], T[i] = T[i], T[parent(i)]
        i = parent(i)