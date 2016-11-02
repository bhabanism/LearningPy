def printFile(fileName):
    file = open(fileName)
    for line in file.readlines():
        print(line, end='')


print("hello hell!")

i = 0
while i < 10 :
    i = i + 1

print("i = {}.".format(i))

for r in range(10) :
    i = i - r    
    print("i = {}.".format(i))

printFile("junk.txt")



