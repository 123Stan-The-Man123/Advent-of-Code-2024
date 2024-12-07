def main():
    similarity_score = 0
    list1 = []
    list2 = []

    with open ("./input.txt", 'r') as file:
        for line in file:
            line = line.split(" ")
            list1.append(line[0])
            list2.append(line[-1][:-1])

    for item in list1:
        amount = list2.count(item)
        similarity_score += int(item) * amount

    print(similarity_score)

main()
