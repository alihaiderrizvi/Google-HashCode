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

    with open('d_pet_pictures.txt') as file:
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
        print(maxi, mini)
                
    return newans
hori , ver = orientation(openk())
