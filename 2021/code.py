file1 = 'a.txt'
file2 = 'b.txt'
file3 = 'c.txt'
file4 = 'd.txt'
file5 = 'e.txt'
file6 = 'f.txt'

import math
from collections import defaultdict
import random

def readfile(filename):
    file = open(filename, 'r')
    line = file.readline().split('\n')[0]
    line = line.split()
    D,I,S,V,F = list(map(int, line))

    streets = []
    path = []
    for i in range(S):
        line = file.readline().split('\n')[0]
        line = line.split()
        line[0] = int(line[0])
        line[1] = int(line[1])
        line[3] = int(line[3])
        streets.append(line)

    for i in range(V):
        line = file.readline().split('\n')[0]
        line = line.split()
        line[0] = int(line[0])
        path.append(line)
    
    return D,I,S,V,F,streets,path

def writefile(filename, data):
    f = open(filename, "w")
    f.write(str(len(data)) + '\n')
    for i in data:
        f.write(str(i) + '\n')
        f.write(str(len(data[i])-1) + '\n')
        for x in range(1, len(data[i])):
            f.write(str(data[i][x][0]) + ' ' + str(data[i][x][1]) + '\n')
    f.close()

# read the file of interest

# D,I,S,V,F,streets,path = readfile(file1)
# D,I,S,V,F,streets,path = readfile(file2)
# D,I,S,V,F,streets,path = readfile(file3)
# D,I,S,V,F,streets,path = readfile(file4)
# D,I,S,V,F,streets,path = readfile(file5)
# D,I,S,V,F,streets,path = readfile(file6)


int_count = {}
intersection = {}
prob_street = defaultdict(int)


for i in path:
    names = i[1:]
    
    for n in names:
        if n not in prob_street:
            prob_street[n] = 1
        else:
            prob_street[n] += 1


for i in prob_street:
    prob_street[i] = prob_street[i] / len(path)

for start, end, street, time in streets:
    
    if end not in intersection:
        int_count[end] = 1
        intersection[end] = [[street, time, start]]

    else:
        int_count[end] += 1
        intersection[end].append([street, time, start])


answer = {}


for i in range(I):
    
    answer[i] = [int_count[i]]
    def_time = 1
    random.shuffle(intersection[i])
    for x in intersection[i]:
        if def_time == 1:
            def_time = -1
        else:
            def_time = 1
        # set the duration of each traffic light
        # tim = (D // len(intersection[i])) + def_time
        # tim = int((D / len(intersection[i])) * (prob_street[x[0]] / I))
        tim = 1
        # if tim <= 0:
        #     tim = 1
        answer[i].append([x[0], tim])

# write the corresponsing file of interest
# writefile('ans_a.txt', answer)
# writefile('ans_b.txt', answer)
# writefile('ans_c.txt', answer)
# writefile('ans_d.txt', answer)
# writefile('ans_e.txt', answer)
# writefile('ans_f.txt', answer)


