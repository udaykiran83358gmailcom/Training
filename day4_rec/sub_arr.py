def sub_arr(arr,st,end):
    if st==len(arr):
        return
    if end==len(arr):
        sub_arr(arr,st+1,st+1)
    else:
        print(arr[st:end+1])
        sub_arr(arr,st,end+1)
        
    
arr=[1,2,3]
sub_arr(arr,0,0)
