# file = open(r'005.test1.txt', 'r')
file = open(r'005.real.txt', 'r')
A,B = file.readlines()

def get_points(route):
    route = route.replace('\n','')
    commands = route.split(',')
    points = {} 
    x, y = 0, 0
    l = 0 
    for command in commands:
        direction = command[0]
        steps = command[1:]
        for _ in range(int(steps)):
            if direction == 'U':
                y = y + 1
            if direction == 'D':
                y = y - 1
            if direction == 'L':
                x = x - 1
            if direction == 'R':
                x = x + 1
            l = l + 1
            if (x,y) not in points:
                points[(x, y,)] = l
    return points

A = get_points(A)
B = get_points(B)
both = set(A.keys())&set(B.keys())
print(min([abs(x) + abs(y) for (x,y) in both]))
print(min([A[p]+B[p] for p in both]))
