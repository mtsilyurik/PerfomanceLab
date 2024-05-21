import sys

n = int(sys.argv[1])
m = int(sys.argv[2])

list_ = [_ for _ in range(1, n + 1)]

t = [0]
res = []

while t[-1] != 1:
    t = list_[0:m]
    res.append(t[0])
    list_ = list_[m - 1:] + list_[0:m - 1]

print(*res, sep='')
