def freq(a,dic,i):
    if i==len(a):
        return max(dic,key=dic.get)
    dic[a[i]]=dic.get(a[i],0)+1
    return freq(a,dic,i+1)
a=[1,1,1,2,2,3]
dic={}
print(freq(a,dic,0))
print(dic)