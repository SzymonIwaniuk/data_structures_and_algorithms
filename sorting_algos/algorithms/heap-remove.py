from heapsort import heapify

def heap_remove(T):
    if len(T) == 0:
        return None

    T[0], T[-1] = T[-1], T[0]
    max_elem = T.pop() 

    heapify(T, 0, len(T))
    
    return max_elem