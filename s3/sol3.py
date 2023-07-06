def solve(l):
    dict = {}
    for i in l:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    
    for i,count in dict.items():
        if i in dict and dict[i]>=2:
            return True
    return False



l1 = [1,2,4,5,6,7]
l2 = [3,3,6,7,7,7,7,5,1]

print(solve(l1))
print(solve(l2))


