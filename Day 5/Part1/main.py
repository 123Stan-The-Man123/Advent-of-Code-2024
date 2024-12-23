def find_middle(line):
    length = len(line) - 1
    return int(line[int(length/2)])

def check_valid(rules, line):
    line = line.split(',')
    for rule in rules:
        try:
            if (int(line.index(rule[0])) > int(line.index(rule[1]))):
                return 0
        except ValueError:
            pass

    return find_middle(line)

def main():
    rules = []
    lines = []

    with open("./input.txt", 'r') as file:
        for line in file:
            if ((line.count("|")) == 1):
                rules.append(line.strip().split('|'))
            else:
                if (line != '\n'):
                    lines.append(line)

    total = 0
    for line in lines:
        total += check_valid(rules, line)

    print(total)

main()
