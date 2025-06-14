from typing import List, Tuple


def reklamy(T: List[Tuple[int, int]], S: List[int], o: int) -> int:
    n = len(T)

    companies_with_prices = [(T[i][0], T[i][1], S[i]) for i in range(n)]
    companies_with_prices.sort(key=lambda x: (x[0], x[1]))
    print(companies_with_prices)

    n = len(companies_with_prices)
    max_revenue = 0

    for i in range(n - 1):
        current_revenue = companies_with_prices[i][2]
        prev = companies_with_prices[i][1]

        for j in range(i + 1, n):
            current_start = companies_with_prices[j][0]
            current_end = companies_with_prices[j][1]

            if prev < current_start and current_end <= o:
                current_revenue += companies_with_prices[j][2]
                prev = current_end

        max_revenue = max(max_revenue, current_revenue)

    return max_revenue


if __name__ == "__main__":
    T = [(0, 3), (4, 5), (1, 4)]
    S = [5000, 3000, 15000]
    o = 6
    print(reklamy(T, S, o))
