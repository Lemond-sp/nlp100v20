import matplotlib.pyplot as plt
import re


def read_score(filename):
    with open(filename) as f:
        line = f.readlines()[1]
        line = re.search(r"(?<=BLEU4 = )\d*\.\d*(?=,)", line)
        return float(line.group())


x = range(1, 21)
y = [read_score(f"contents/results/kyoto.dev.{n_beam}.txt") for n_beam in x]
plt.plot(x, y)
plt.show()
