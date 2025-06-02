from collections import defaultdict
graph=((5,2),(5,7),(5,8),(2,7),(2,8),(8,7),(8,3),(2,3))
d=defaultdict(list)
def paths(u,v,path=[]):
    path.append(u)
    if u==v:
        print(path)
        # path.pop()
       
    for i in d[u]:
        if i not in path:
            paths(i,v,path)
    path.pop()
    return


for i,j in graph:
    # if i not in d:
    #     d[i]=[j]
    # else:
    #     d[i].append(j)
    # if j not in d:
    #     d[j]=[i]
    # else:
    #     d[j].append(i)

    d[i].append(j)
    d[j].append(i)
print(d)
paths(5,3)



