
data = [line.strip() for line in open("input1.txt", "r").readlines()]

def first_star():
    global data
    total = 0
    first = []
    second = []
    for line in data:
        nums = line.split("   ")
        first.append(int(nums[0]))
        second.append(int(nums[1]))
    first = sorted(first)
    second = sorted(second)

    for i in range(len(first)):
        total += abs(second[i] - first[i])

    return total

def second_star():
    global data
    total = 0
    amount = {}
    first = []
    second = []
    for line in data:
        nums = line.split("   ")
        first.append(int(nums[0]))
        second.append(int(nums[1]))
    
    for num in second:
        if num in amount:
            amount[num] += 1
        else:
            amount[num] = 1

    for num in first:
        if num in amount:
            total += num * amount[num]
    
    return total

if __name__ == "__main__":
    print(first_star(), second_star())
