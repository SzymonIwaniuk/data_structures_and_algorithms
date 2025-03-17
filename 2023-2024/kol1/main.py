"""
Dana jest n-elementowa tablica liczb naturalnych T. Dla każdego indeksu i < n, rangą elementu
na pozycji i określamy liczbę elementów, które w tablicy występują przed elementem i-tym, a ich
wartość jest mniejsza od T [i]. Proszę zaimplementować funkcję maxrank(T), która dla tablicy T o
rozmiarze n elementów zwróci maksymalną rangę pośród wszystkich elementów tablicy
"""


class BSTNode:
    def __init__ (self,val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.leftsize = 0


def max_rank(T):

    maxi = 0
    cur = BSTNode(T[0])
    n = len(T)

    for i in range(1,n): # Przejscie po tablicy O(n)
        cnt = 0
        copy = cur

        while True: # Wstawienie elemetnu do drzewa O(logn)

            if copy.val >= T[i]:

                copy.leftsize += 1

                if copy.left == None:
                    copy.left = BSTNode(T[i])
                    break

                else:
                    copy = copy.left
            else:

                cnt += copy.leftsize + 1
                if copy.right == None:
                    copy.right = BSTNode(T[i])
                    maxi = max(cnt,maxi)
                    break

                else:
                    copy = copy.right

    return maxi

    #Calosc O(nlogn)


print(max_rank([5,3,9,4]))