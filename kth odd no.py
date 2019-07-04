# kth-odd-noo
i,j=map(int,input().split())
d=list(map(int,input().split()))[:i]
c=0
for o in d:
    if o%2!=0:
        c+=1
        if c==j:
            print(o)
