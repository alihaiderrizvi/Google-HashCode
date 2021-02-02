def orientation(final_matrix):
    horizontal = []
    vertical = []
    for x in final_matrix:
        if x[0] == "H":
            horizontal.append(x)
        else:
            vertical.append(x)
    return horizontal, vertical


def insertion_sort(lst):
    for i in range(len(lst)):
        if len(lst) == 1:
            # print(lst)
            return
        counter = i
        val = lst[counter]
        while counter > 0:
            if val[0] < lst[counter - 1][0]:
                lst[counter] = lst[counter - 1]
                counter -= 1
            else:
                break
        lst[counter] = val
    return lst


def openk():

    with open('b_lovely_landscapes.txt') as file:
        ans = []
        newans = []
        a=-1
        for x in file:

            word = x.split() + [a]
            ans.append(word)

            a+=1
        maxi = 0
        mini  = 1000000000000000
        for y in ans:
            if len(y) > maxi:
                maxi = len(y)
            if len(y) > 2 and len(y) < mini:
                mini = len(y)

        while maxi >= mini:
            for z in ans:
                if len(z) == maxi:
                    newans.append(z)
            maxi -= 1
                
    return newans
hori , ver = orientation(openk())


def sort_(ans):
    combination = []
    for x in range(len(ans)):
        for i in range(x+1 , len(ans)):
            commonalities = set(ans[x][2:-1]) - (set(ans[x][2:-1]) - set(ans[i][2:-1]))
            if len(commonalities) >0:
                print(str(ans[x][-1]))
                print(str(ans[i][-1])) 
                ans.pop(i)
                # print(x, i)
                break
    return combination
def sort1(ans):
    combination = []
    for x in range(len(ans)):
        for i in range(x+1 , len(ans)):
            commonalities = set(ans[x][2:-1]) - (set(ans[x][2:-1]) - set(ans[i][2:-1]))
            if len(commonalities) >0:
                print(str(ans[x][-1]) + " " +(str(ans[i][-1])) )
                ans.pop(i)
                # print(x, i)
                break
    return combination
##hori , ver = orientation(final_matrix)
##ans = insertion_sort(openk())
dhuz = sort_(hori)

# print(dhuz)
##u = str(len(dhuz)*2)
##for w in range(len(dhuz)):
##    u+=dhuz[w][0] + '\n'
##    u += dhuz[w][1] + '\n'
##print(u)
dhuzdhuz= sort1(ver)
##print(dhuzdhuz)
##v  = str(len(dhuzdhuz)) + '\n'

##for z in range(len(dhuzdhuz)):
##    print(dhuzdhuz)
##    v+=dhuzdhuz[z][0] + ' ' + dhuzdhuz[z][1] + '\n'
    
##print(v)


# print(dhuz[:])
# def commonpair(ans):
#     for x in range(len(ans)):
#         for y in range(len(ans)):
#             if
