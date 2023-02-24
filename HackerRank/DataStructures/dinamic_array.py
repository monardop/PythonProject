def dynamicArray(n: int, queries: list):
    la=0
    ans=[]
    arr =[[] for _ in range(n)]
    for i in queries:
        print(i)
        if i[0]==1:
            idx=((i[1]^la)%n)
            arr[idx].append(i[2])
        elif i[0]==2:
            idx=((i[1]^la)%n)
            la=arr[idx][i[2]%len(arr[idx])]
            ans.append(la)
    return(ans)