n=[1,2,3,4,5,6]
tar=11
st=0
curr=0
min_len=999
for i in range(len(n)):
    curr+=n[i]
    while curr>=tar:
        if min_len>i-st+1:
            min_len=i-st+1
            x,y=st,i 
        
        curr-=n[st]
        st+=1
   
print(min_len)
print(n[x],n[y])
    
# def value_sort(x):
#     return x[1]
# a=[0,3,8,1,5,7,9]
# b=[5,6,10,2,6,9,11]
# t=list(zip(a,b))
# print(t)
# t.sort(key=value_sort)
# st=0
# c=0
# for i in t:
#     if(i[0]>=st):
#         c=c+1
#         st=i[1]+1
# print(c)