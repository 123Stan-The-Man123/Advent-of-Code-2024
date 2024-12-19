def search(lines, i, j):
    if (i < 1 or j < 1):
        return 0

    try:
        if (((lines[i-1][j-1] == 'M' and lines[i+1][j+1] == 'S') or (lines[i-1][j-1] == 'S' and lines[i+1][j+1] == 'M')) and ((lines[i+1][j-1] == 'M' and lines[i-1][j+1] == 'S') or (lines[i+1][j-1] == 'S' and lines[i-1][j+1] == 'M'))):
            return 1
    except IndexError:
        pass
    
    return 0

def find_xmas(lines):
    count = 0

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if (lines[i][j] == 'A'):
                count += search(lines, i, j)
    
    return count

def main():
    lines = []
    with open("./input.txt", 'r') as file:
        for line in file:
            lines.append(line)
    
    print(find_xmas(lines))

main()