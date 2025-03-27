# adaptacja algorytmu sortowania przez scalania
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

    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            res.next = l1
            l1 = l1.next
        else:
            res.next = l2
            l2 = l2.next
        res = res.next

    if l1 is not None:
        res.next = l1
    if l2 is not None:
        res.next = l2

    return result.next


# odcinanie serii uporządkowanych liczb naturalnych (np. z 1->2->5->0->2 odcinamy 1->2>5) z linked listy
def l_cut(l):
    if not l:
        return None, None

    res = Node(-float("inf"))
    tail = res

    while l is not None and (tail.val <= l.val):
        v = l
        l = l.next
        tail.next = v
        tail = tail.next
        tail.next = None

    return res.next, l


def l_sort(l):
    if not l or not l.next:
        return l

    while True:
        cnt = 0
        P = Node(None)
        tail = P
        while l is not None:
            s1, l = l_cut(l)
            cnt += 1
            if l is None:
                tail.next = s1
                break
            s2, l = l_cut(l)
            cnt += 1
            s = l_merge(s1, s2)
            tail.next = s
            while tail.next is not None:
                tail = tail.next
        l = P.next

        if cnt <= 1:
            return l

a = Node(5,Node(3,Node(2,Node(10,Node(5,Node(1,Node(2,Node(3,Node(4)))))))))
p = l_sort(a)
print_list(p)

