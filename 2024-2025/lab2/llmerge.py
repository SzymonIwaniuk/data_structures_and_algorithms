 adaptacja algorytmu sortowania przez scalania
# algorytm znajduje w linked liscie kolejne serie naturalne (seria naturalne to niemalejacy ciag liczb) i odpina je parami
# algorytm scala parami listy
# postępujemy w ten sposob, do póki aż lista nie będzie składać się dokładnie z jednej serii naturalnej
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def print_list(x):
    while x:
        print(x.val, end=" -> ")
        x = x.next

# scalanie dwoch posortowanych list
def l_merge(l1, l2):
    result = Node(0)
    res = result
    while l1.next is not None and l2.next is not None:
        if l1.next.val < l2.next.val:
            res.next = l1.next
            l1 = l1.next
        else:
            res.next = l2.next
        res = res.next
    if l1 is not None:
        res.next = l1
    if l2 is not None:
        res.next = l2
    return result


# odcinanie serii uporządkowanych liczb naturalnych (np. z 1->2->5->0->2 odcinamy 1->2>5) z linked listy
def l_cut(l):
    res = Node(-float("inf"))
    tail = res
    while l.next is not None:
        if res.next is None or tail.val <= l.next.val:
            v = l.next
            l.next = l.next.next
            tail.next = v
            tail = tail.next
            v.next = None
        else:
            return res

def l_sort(l):
    while True:
        cnt = 0
        P = Node(None)
        tail = P
        while l.next is not None:
            s1 = l_cut(l)
            cnt += 1
            if l.next is None:
                tail.next = s1.next
                l.next = P.next
                break
            s2 = l_cut(l)
            cnt += 1
            s = l_merge(s1,s2)
            tail.next = s.next
            while tail.next is not None:
                tail = tail.next
            if l.next is None:
                l.next = P.next
                break
        if cnt <= 2:
            return l
