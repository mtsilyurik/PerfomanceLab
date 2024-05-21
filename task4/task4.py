import sys


file_path = sys.argv[1]

with open(file_path, "r") as f:
    list_ = list(map(lambda x: int(x), f.read().splitlines()))

list_.sort()

pivot = list_[len(list_)//2]

res = 0

for i in list_:
    res += abs(pivot-i)

print(res)
