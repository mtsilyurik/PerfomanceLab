import sys


circle_path = sys.argv[1]
points_path = sys.argv[2]

with open(circle_path, 'r') as circle_file:
    ox_c, oy_c = list(map(lambda x: int(x),
                          circle_file.readline()
                          .replace('\n', '')
                          .replace(' ', '')))

    radius = float(circle_file.readline())


with open(points_path, 'r') as points_file:
    points = points_file.readlines()


for point in points:
    ax, ay = map(lambda x: int(x), point.replace('\n', '').split())
    dest = ((ox_c - ax) ** 2 + (oy_c - ay) ** 2) ** 0.5
    if dest < radius:
        print(1)
    elif dest > radius:
        print(2)
    elif dest == radius:
        print(0)
