p = [6, 5, 8, 9, 6, 7, 3]
v = [2, 3, 6, 7, 5, 9, 4]
n = len(p)

states = [(n - 1, 9)]
take = []
ntake = []

for i in range(n - 1, -1, -1):
    for state in states:
        if state[0] == i:
            states.append((i - 1, state[1]))
            ntake.append((i, state[1], i - 1, state[1]))
            if state[1] - p[i] >= 0:
                states.append((i - 1, state[1] - p[i]))
                take.append((i, state[1], i - 1, state[1] - p[i]))


states = sorted(list(set(states)))
take = sorted(list(set(take)))
ntake = sorted(list(set(ntake)))


for i, c in states:
    print(f'\drawState{{{i}}}{{{c}}}')

for a, b, c, d in ntake:
    print(f'\\ntake{{E_{a}_{b}}}{{E_{c}_{d}}}')


for a, b, c, d in reversed(take):
    print(f'\\take{{E_{a}_{b}}}{{E_{c}_{d}}}{{{b - d}}}')
