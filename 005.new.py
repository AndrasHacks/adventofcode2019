file = open(r'005.real.txt', 'r')
lines = file.readlines()
wire1 = lines[0].replace('\n', '').split(',')
wire2 = lines[1].replace('\n', '').split(',')
# print(wire1, wire2)

def draw_wire(wire, space, symbol, wx, wy):
    for i in range(len(wire)):
        for j in range(int(wire[i][1:])):
            if wire[i][0] == 'U':
                wx = wx - 1
            elif wire[i][0] == 'D':
                wx = wx + 1
            elif wire[i][0] == 'L':
                wy = wy - 1
            elif wire[i][0] == 'R':
                wy = wy + 1
            if space[wx][wy] != symbol and space[wx][wy] != '.' and space[wx][wy] != '0': 
                space[wx][wy] = 'X'
            else:
                space[wx][wy] = symbol
    return space

def get_x_sections(space):
    crosses = []
    for row in range(len(space)):
        for column in range(len(space[row])):
            if space[row][column] == 'X':
                crosses.append([row, column])
    return crosses

width = 25000
height = 25000
space = [['.' for x in range(width)] for y in range(height)] 
origo_x = width // 2
origo_y = height // 2
space[origo_x][origo_y] = 'O'
space = draw_wire(wire1, space, '1', origo_x, origo_y)
space = draw_wire(wire2, space, '2', origo_x, origo_y)
cross_sections = get_x_sections(space)
manhattan_distances = []
for x in range(len(cross_sections)):
    manhattan_distances.append(abs(origo_y - cross_sections[x][0]) + abs(origo_x - cross_sections[x][1]))
#for i in range(width):
#    for j in range(height):
#        print(space[i][j], end='')
#    print('\n')

print(min(manhattan_distances))

    
