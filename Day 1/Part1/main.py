def main():
    total = 0
    list1 = []
    list2 = []

    with open ("./input.txt", 'r') as file:
        for line in file:
            line = line.split(" ")
            list1.append(line[0])
            list2.append(line[-1])

    while (list1 != []):
        min1 = min(list1)
        min2 = min(list2)
        
        if (min2 > min1):
            difference = int(min2) - int(min1)
        else:
            difference = int(min1) - int(min2)

        total += difference
        list1.remove(min1)
        list2.remove(min2)

    print(total)

main()
