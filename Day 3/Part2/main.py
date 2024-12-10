import re

def multiplication(item):
    numbers = re.findall("\d+", item)
    multiplication = int(numbers[0]) * int(numbers[1])
    return multiplication
    
def main():
    temp_multiplications = []
    with open("input.txt", 'r') as file:
        for line in file:
            temp_multiplications.append(re.findall("(mul\(\d+,\d+\)|do\(\)|don't\(\))", line))

    multiplications = []
    do = True
    
    for line in temp_multiplications:
        temp = []
        for item in line:
            if (item == "do()"):
                do = True
            elif (item == "don't()"):
                do = False

            if (do and item[0] == 'm'):
                temp.append(item)

        multiplications.append(temp)
            
    sum = 0
    for line in multiplications:
        for item in line:
            sum += multiplication(item)

    print(sum)

main()
