def search(lines, i, j):
    total = 0
    temp = "X"

    # right
    try:
        temp += lines[i][j+1] + lines[i][j+2] + lines[i][j+3]
        if (temp == "XMAS"):
            total += 1
    except IndexError:
        pass

    temp = "X"

    # left
    try:
        if (j > 2):
            temp += lines[i][j-1] + lines[i][j-2] + lines[i][j-3]
            if (temp == "XMAS"):
                total += 1
    except IndexError:
        pass

    temp = "X"

    # up
    try:
        temp += lines[i+1][j] + lines[i+2][j] + lines[i+3][j]
        if (temp == "XMAS"):
            total += 1
    except IndexError:
        pass

    temp = "X"

    # down
    try:
        if (i > 2):
            temp += lines[i-1][j] + lines[i-2][j] + lines[i-3][j]
            if (temp == "XMAS"):
                total += 1
    except IndexError:
        pass

    temp = "X"

    # Up-right
    try:
        temp += lines[i+1][j+1] + lines[i+2][j+2] + lines[i+3][j+3]
        if (temp == "XMAS"):
            total += 1
    except IndexError:
        pass

    temp = "X"

    # Up-left
    try:
        if (j > 2):
            temp += lines[i+1][j-1] + lines[i+2][j-2] + lines[i+3][j-3]
            if (temp == "XMAS"):
                total += 1
    except IndexError:
        pass

    temp = "X"

    # Down-left
    try:
        if (i > 2 and j > 2):
            temp += lines[i-1][j-1] + lines[i-2][j-2] + lines[i-3][j-3]
            if (temp == "XMAS"):
                total += 1
    except IndexError:
        pass

    temp = "X"

    # Down-right
    try:
        if (i > 2):
            temp += lines[i-1][j+1] + lines[i-2][j+2] + lines[i-3][j+3]
            if (temp == "XMAS"):
                total += 1
    except IndexError:
        pass

    return total

def find_xmas(lines):
    count = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if ((lines[i][j]) == 'X'):
                count += search(lines, i, j)

    return count

def main():
    lines = []
    with open("input.txt", 'r') as file:
        for line in file:
            lines.append(line)

    print(find_xmas(lines))
    
main()
