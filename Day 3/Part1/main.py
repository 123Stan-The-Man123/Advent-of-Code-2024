import re

def multiplication(item):
    numbers = re.findall("\d+", item)
    multiplication = int(numbers[0]) * int(numbers[1])
    return multiplication
    
def main():
    multiplications = []
    with open("input.txt", 'r') as file:
        for line in file:
            multiplications.append(re.findall("mul\(\d+,\d+\)", line))

    sum = 0
    for line in multiplications:
        for item in line:
            sum += multiplication(item)

    print(sum)

main()
