from random import randint

MIN = 10
MAX = 20

positions = {(randint(0, MIN), randint(0, MIN)) for _ in range(MAX)}

while len(positions) < MAX:
    positions |= {(randint(0, MIN), randint(0, MIN))}

positions = list(list(x) for x in positions)


def get_ordered_list(positions: list, x: int, y: int):
   return sorted(positions, key = lambda p: (p[0] - x)**2 + (p[1] - y)**2)


test = get_ordered_list(positions, 0, 0)
print(test)





from matplotlib import pyplot as plt
import numpy as np

plt.plot([i[0] for i in test],[i[1] for i in test], 'ro', alpha = 0.5)
for i in range(len(test)):
    print(test[i])
    plt.text(test[i][0], test[i][1], str(i))

plt.show()