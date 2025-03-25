"""
Woda spływa z kranu do zbiorników, które są połączone rurami.
Zbiornik jest opisany krotką z górną i dolną wysokością danego zbiornika (górna jest pierwsza).
Pole przekroju danego zbiornika to 1 m2. Woda zawsze spłynie na sam dół.
Mamy podaną ilość m3 wody jako l i mamy podać, do jakiej wysokości woda zapełni zbiorniki.
Wysokości są zmiennoprzecinkowe.
"""

"""
Definiujemy funkcję L(h), która zwróci ilość wody, którą trzeba nalać, aby zapełnić zbiorniki do
podanej wysokości. Potem metodą bisekcji szukamy takiego h, dla którego funkcja L(h) da rozwiązanie bliskie l.
Dzięki temu znajdziemy wysokość, o którą nas pytają.
"""


def L(T, h):
    s = 0
    for top, bottom in T:

        if bottom < h < top:
            s += h - bottom

        elif h >= top:
            s += top - bottom

        return s


def h(T, l):
    eps = 1e-10
    a = 0

    b = max(T, key=lambda x: x[0])[0]
    mid = (a + b) / 2

    while b - a > eps:
        mid = (a + b) / 2

        if L(T, mid) >= l:
            b = mid
        else:
            a = mid

    return mid


if __name__ == "__main__":
    T = [(2.5, 0.0), (4.2, 1.5), (8.1, 6.0)]
    print(h(T, 5.3))
