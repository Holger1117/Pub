import re
data = "".join(open("input.txt").readlines())
total = 0

def mul(a, b):
    return a * b

inst = re.findall(r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))", data)
go = True
for i in inst:
    if i[0] == "do()":
        go = True
    elif i[0] == "don't()":
        go = False
    else:
        if go == True:
            print(i)
            total += mul(int(i[1]), int(i[2]))

print(total)