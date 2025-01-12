def find_guard(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if (map[i][j] == '^'):
                return [i, j]

def change_direction(offsets):
    if (offsets[0] == -1):
        offsets[0] = 0
        offsets[1] = 1
    elif (offsets[1] == 1):
        offsets[1] = 0
        offsets[0] = 1
    elif (offsets[0] == 1):
        offsets[0] = 0
        offsets[1] = -1
    else:
        offsets[1] = 0
        offsets[0] = -1

    return offsets

def mark_unique_positions(map, pos, cells):
    offsets = [-1, 0]

    if (cells == 0):
        while ((pos[0] >= 0 and pos[0] < len(map)) and (pos[1] >= 0 and pos[1] < len(map[0]))):
            map[pos[0]] = map[pos[0]][:pos[1]] + 'X' + map[pos[0]][pos[1]+1:]
    
            if ((pos[0] == len(map) - 1) or (pos[1] == len(map[0]) - 1)):
                break
            if (offsets[0] != 0):
                if (map[pos[0] + offsets[0]][pos[1]] == '#'):
                    offsets = change_direction(offsets)
                    pos[1] += offsets[1]
                else:
                    pos[0] += offsets[0]
            else:
                if (map[pos[0]][pos[1] + offsets[1]] == '#'):
                    offsets = change_direction(offsets)
                    pos[0] += offsets[0]
                else:
                    pos[1] += offsets[1]
    
        return map

    else:
        loops = 0
        pos_copy = pos
        for line in range(len(map)):
            for cell in range(len(map[0])):
                if (map[line][cell] == 'X'):
                    pos = pos_copy
                    temp = map[line]
                    map[line] = map[line][:cell] + '#' + map[line][cell+1:]
                    count = 0
                    while ((pos[0] >= 0 and pos[0] < len(map)) and (pos[1] >= 0 and pos[1] < len(map[0])) and count <= cells):
                        count += 1
    
                        if ((pos[0] == len(map) - 1) or (pos[1] == len(map[0]) - 1)):
                            break
                        if (offsets[0] != 0):
                            if (map[pos[0] + offsets[0]][pos[1]] == '#'):
                                offsets = change_direction(offsets)
                                pos[1] += offsets[1]
                            else:
                                pos[0] += offsets[0]
                        else:
                            if (map[pos[0]][pos[1] + offsets[1]] == '#'):
                                offsets = change_direction(offsets)
                                pos[0] += offsets[0]
                            else:
                                pos[1] += offsets[1]
    
                    if (count >= cells):
                        loops += 1
                    
                    map[line] = temp

        return loops

def main():
    map = []
    with open("./input2.txt", 'r') as file:
        for line in file:
            map.append(line.strip())

    start_pos = find_guard(map)
    map = mark_unique_positions(map, start_pos, 0)
    

    cells = 0

    for line in map:
        cells += len(line)

    test = [6, 4]
    print(mark_unique_positions(map, test, cells))

main()
