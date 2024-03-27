

from pprint import pprint


def sac_à_dos(poids, valeurs, capacité):
    cache = {}

    def profit_max(i, c):
        if (i, c) not in cache:
            if i < 0:
                cache[(i, c)] = 0
            elif poids[i] > c:
                cache[(i, c)] = profit_max(i - 1, c)
            else:
                cache[(i, c)] = max(profit_max(i - 1, c), profit_max(i - 1, c - poids[i]) + valeurs[i])
        return cache[(i, c)]

    n = len(poids)
    profit_max(n - 1, capacité)
    pprint(cache)
    return profit_max(n - 1, capacité)


sac_à_dos(
    [6, 5, 8, 9, 6, 7, 3],
    [2, 3, 6, 7, 5, 9, 4],
    9
)
