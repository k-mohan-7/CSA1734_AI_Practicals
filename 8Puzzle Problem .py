n=3
a=[[1,7,4],[2,8,6],[5,3,0]]
k=1
for i in range(0,3):
    for j in range(0,3):
        if(a[i][j]!=k):
            a[i][j]=k
        k=k+1
a[2][2]=0
print(a)
