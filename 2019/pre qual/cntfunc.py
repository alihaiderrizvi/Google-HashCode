def countfunc(lst):
    m = 0
    t = 0
    cnt = 0
    for a in lst:
        for z in a:
            if z == "M":
                
                m += 1
            else:
                t += 1
        print(t, m)
        if m >= 4 and t >= 4:
                cnt += 1
    return cnt

lst = ['TMMMTTTMMMMT', 'MMTTMTTMTTMM', 'TMMMTTTTTTMT', 'TTTTTMMMMMMM', 'TMMMMTTTMTMM', 'TTTTTTMMMMMT', 'TMTMTMMMTMTT', 'MMTTMMMTTMMM', 'TTTTMTTTMTMM', 'MTTMTMTTMTTM', 'TTTTMMMTTTMM', 'TTMMMTTMMTMT', 'MMTTMMTTMTMM', 'MTMMMTMTTMMT', 'MMTTMTTMMMMM', 'TTTMMMTMMMMM', 'MTMTTMTTTTTM', 'MMMMMTMTMMTT', 'TTMMTTTTMTTT', 'MTMMTTMMTMTT', 'MTTTMTMMTM']
print(countfunc(lst))
            
