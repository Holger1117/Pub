data = [line.strip() for line in open("input.txt", "r").readlines()]
def part1():
    count = 0
    for index, line in enumerate(data):
        for i in range(len(line)):
            words = []
            if i < len(line) - 3:
                words.append(line[i] + line[i+1] + line[i+2] + line[i+3])
            if index < len(data) - 3:
                words.append(data[index][i] + data[index + 1][i] + data[index + 2][i] + data[index + 3][i])
                if i < len(line) - 3:
                    words.append(data[index][i] + data[index + 1][i + 1] + data[index + 2][i + 2] + data[index + 3][i + 3])
                if i > 2:
                    words.append(data[index][i] + data[index + 1][i - 1] + data[index + 2][i - 2] + data[index + 3][i - 3])
            for word in words:
                if word == "XMAS" or word[::-1] == "XMAS":
                    count += 1

    return count

def part2():
    count = 0
    for index, line in enumerate(data):
        for i in range(len(line)):
            pairs = []
            if i < len(line) - 2 and index < len(data) - 2:
                pairs.append([data[index][i] + data[index + 1][i + 1] + data[index + 2][i + 2], data[index][i + 2] + data[index + 1][i + 1] + data[index + 2][i]])
            for words in pairs:
                if (words[0] == "MAS" or words[0][::-1] == "MAS") and (words[1] == "MAS" or words[1][::-1] == "MAS"):
                    count += 1
    return count

print(part1())
print(part2())
