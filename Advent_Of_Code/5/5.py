data = [line.strip() for line in open("input5.txt", "r").readlines()]
def part1():
    x_list = []
    y_list = []
    updates = []
    total = 0
    for line in data:
        if "|" in line:
            x, y = line.strip().split("|")
            x_list.append(int(x))
            y_list.append(int(y))
        if "," in line:
            updates.append([int(num) for num in line.strip().split(",")])

    for update in updates:
        seen_pages = []
        correct = True
        for page in update:
            for i in range(len(x_list)):
                if x_list[i] == page:
                    if y_list[i] in seen_pages:
                        correct = False
                        break
            
            if correct == False:
                break
            seen_pages.append(page)
        if correct == True:
            total += update[int(len(update)/2)]
    return total

def part2():
    x_list = []
    y_list = []
    updates = []
    total = 0
    for line in data:
        if "|" in line:
            x, y = line.strip().split("|")
            x_list.append(int(x))
            y_list.append(int(y))
        if "," in line:
            updates.append([int(num) for num in line.strip().split(",")])

    for update in updates:
        seen_pages = []
        correct = True
        for page in update:
            for i in range(len(x_list)):
                if x_list[i] == page:
                    if y_list[i] in seen_pages:
                        correct = False
                        break
            
            if correct == False:
                break
            seen_pages.append(page)
        if correct == False:
            new_update = []
            for page in update:
                for index, new in enumerate(new_update):
                    length = len(new_update)
                    for i in range(len(x_list)):
                        if x_list[i] == page and y_list[i] == new:
                            new_update.insert(index, page)
                            break
                    if len(new_update) > length:
                        break
                else:
                    new_update.append(page)
            total += new_update[int(len(new_update)/2)]

    return total

print(part1())
print(part2())