def openk1():

    with open('b_lovely_landscapes.txt') as file:
        ans = []
        newans = []
        a=-1
        for x in file:

            word = x.split() + [a]
            ans.append(word)

            a+=1
        return ans

lst = openk1()
#print("ok")
score = 0
#print(lst[80004])
a = int(input())
b = int(input())
for x in range(76409):
    try:
        tags1 = lst[a][2:-1]
        tags2 = lst[b][2:-1]
        common = len(list(set(tags1).intersection(tags2)))
        uniq1 = abs(len(tags1[2:-1]) - common)
        uniq2 = abs(len(tags2[2:-1]) - common)
        score += min(common, uniq1, uniq2)
        a = b
        b = int(input())
        print(score)
    except:
        print(b)

print(score)
