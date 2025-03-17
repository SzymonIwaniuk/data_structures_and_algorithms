# Sortowanie przez wstawianie;
# Złożoność: O(N^2)

def insrtion_sort(T):
    n = len(T)
    for i in range(1,n):
        for j in range(i,0,-1):
            if T[j] < T[j-1]:
                T[j][j-1] = T[j-1][j]
            else:
                break
    return T #można nic nie zwracać ( list jest przekazana przez referencję )


# Odpięcie minimum od linked listy
#( przekazany jest wartownik, nie pierwszy element listy )

class Node:
    def __init__ (self,val,next=None):
        self.val = val
        self.next = next

def find_min(head):
    if head is None or head.next is None:   return None
    min = float('inf')
    v = head
    while head.next is not None:
        if head.next.val < min:
            min = head.next.val
            v = head
        head = head.next
    return v.next # Zwracamy wskaźnik na najmniejszy element


# Ta sama funkcja ale tym razem zwracamy listę bez minimum
#( przekazany jest wartownik, nie pierwszy element listy )

def remove_min(head):
    if head is None or head.next is None:   return None
    min = float('inf')
    v = head
    while head.next is not None:
        if head.next.val < min:
            min = head.next.val
            v = head
        head = head.next
    res = v
    v.next = v.next.next
    return res


# Wpięcie elementu(wskaźnika) do posortowanej linked listy
#( przekazany jest wartownik, nie pierwszy element listy )

def insert(head, v):
    cur = head
    while cur.next != None:
        if cur.next.val > v.val:
            v.next = cur.next
            cur.next = v
            return head
        cur = cur.next


# Znajdowanie najmniejszego i największego elemntu w liście;
# Złożoność: O(3N/2)

def find_M_m(T):
    n = len(T)
    mini = T[0]
    maksi = T[0]
    for i in range(0,n-1,2):
        if T[i] < T[i+1]:
            if T[i] < mini:
                mini = T[i]
            elif T[i+1] > maksi:
                maksi = T[i+1]
        else:
            if T[i] > maksi:
                maksi = T[i]
            elif T[i+1] < mini:
                mini = T[i+1]
    return mini,maksi

# Sortowanie linked listy z użyciem poprzednich funkcji
#( przekazany jest wartownik, nie pierwszy element listy )

def sorting(head):
    if head is None or head.next is None:   return head
    w = Node(head.val)
    start = w
    while head.next != None:
        v = find_min(head)
        w.next = v
        remove_min(head)
        w = w.next
    return start


# Przesuwanie elementów listy o 'k' znaków

def swap(T,k):
    n = len(T)
    for i in range(k):
        T[i],T[k+i] = T[k+i],T[i]
    limit = n - 2*k
    counter = 0
    while counter < limit:
        for j in range(n-limit+counter,k+counter,-1):
            T[j],T[j-1] = T[j-1],T[j]
        counter += 1
    