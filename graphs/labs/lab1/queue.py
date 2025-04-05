"""
Prosze zaimplementowac kolejke w zamortyzowanym czasie O(1) majac do wykorzystania
dwa stosy
"""

"""
Majac dwa stosy gdy chcemy pobrac element z kolejki przerzucamy wszystkie elementy
z jednego stosu na drugi (pusty) i pobieramy z niego elementy az do jego opustoszenia.
Natomiast kiedy chcemy dodac element do kolejki, dodajemy ten element na pierwszy stos.
"""


class Queue:
    def __init__(self, n):
        self.stack1 = [0] * n
        self.stack2 = [0] * n
        self.top1 = 0
        self.top2 = 0
        self.capacity = n

    def pop(self):
        if self.top1 == 0 and self.top2 == 0:
            raise Exception("queue is empty")

        else:
            if self.top2 == 0:
                # Przerzucamy elementy z jedngo stosu do drugiego
                while self.top1 > 0:
                    self.top1 -= 1
                    self.stack2[self.top2] = self.stack1[self.top1]
                    self.top2 += 1

            self.top2 -= 1
            val = self.stack2[self.top2]
            self.stack2[self.top2] = 0
            return val

    # Dodawanie elementu
    def add(self, x):
        if self.top1 > self.capacity:
            raise Exception("queue is full")
        self.stack1[self.top1] = x
        self.top1 += 1


if __name__ == "__main__":
    Q = Queue(10)

    for i in range(1, 4):
        Q.add(i)

    for j in range(3):
        print(Q.pop())
