def buy(n,i,k):
    if i==len(n):
        return
    s=n[i]
    sell(n,i+1,s,k)
    buy(n,i+1,k)
def sell(n,j,s,k):
    if j==len(n):
        return
    if n[j]-s>=0:
        k.append(n[j]-s)
    sell(n,j+1,s,k)

n=list(map(int,input().split()))
k=[]
buy(n,0,k)
print(max(k))
maxi=0
b=n[0]
p=0
for i in range(1,len(n)):
    p=max(p,n[i]-b)
    if b>n[i]:
        n[i]=b
print(p)








# maxi,mini=n[0],n[0]
# for i in n:
#     if i<mini:
#         mini=i
#     if i>maxi:
#         maxi=i
# maxi=
# for i in range(len(n)):
    




# print("profit",maxi-mini)

