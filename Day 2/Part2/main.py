def check_safety(report):
    if (int(report[1]) > int(report[0])):
        increasing = True
    elif (int(report[0]) > int(report[1])):
        increasing = False
    else:
        return False
    
    for i in range(len(report) - 1):
        if (int(report[i+1]) > int(report[i]) and increasing):
            difference = int(report[i+1]) - int(report[i])
            if (difference > 3):
                break
            if (i == len(report) - 2):
                return True
            continue
        if (int(report[i+1]) <= int(report[i]) and increasing):
            break
        if (int(report[i]) > int(report[i+1]) and not(increasing)):
            difference = int(report[i]) - int(report[i+1])
            if (difference > 3):
                break
            if (i == len(report) - 2):
                return True
            continue
        else:
            break

    return False

def main():
    safe_count = 0
    reports = []

    with open("./input.txt", 'r') as file:
        for report in file:
            report = report.split(" ")
            report[-1] = report[-1][:-1]
            reports.append(report)

    for report in reports:
        safe = False

        safe = check_safety(report)

        while (not(safe)):
            for i in range(len(report)):
                temp_report = []
                for j in range (len(report)):
                    if (i != j):
                        temp_report.append(report[j])
                safe = check_safety(temp_report)
                if (safe):
                    break
            break
            
        if (safe):
            safe_count += 1

    print(safe_count)

main()
