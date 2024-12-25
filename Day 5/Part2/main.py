def find_middle(line):
    length = len(line) - 1
    return int(line[int(length/2)])

def fixed_line(rules, line):
    adjustment = False

    for rule in rules:
        try:
            if (line.index(rule[0]) > line.index(rule[1])):
                adjustment = True
                temp_index = line.index(rule[0])
                temp = line[temp_index]
                original_index = line.index(rule[1])
                original = line[original_index]
                
                line[temp_index] = original
                line[original_index] = temp
        
        except ValueError:
            pass

    if (adjustment):
        return fixed_line(rules, line)
    return line

def check_valid(rules, line):
    line = line.split(',')
    for rule in rules:
        try:
            if (line.index(rule[0]) > line.index(rule[1])):
                return find_middle(fixed_line(rules, line))
        except ValueError:
            pass

    return 0

def main():
    rules = []
    lines = []

    with open("./input.txt", 'r') as file:
        for line in file:
            if ((line.count("|")) == 1):
                rules.append(line.strip().split('|'))
            else:
                if (line != '\n'):
                    lines.append(line.strip())

    total = 0
    for line in lines:
        total += check_valid(rules, line)

    print(total)

main()
