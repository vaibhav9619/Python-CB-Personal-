n=int(input())
l=list(map(int,input().split()))[:n]
s=l[0]
x=[0]*n
for i in range(1,n):

    # s=x[i-1]
    if l[i] > s:
        a=l[i]
        for j in range(i,n-1):
            x[j]=x[j+1]
        x[i]=a
    elif l[i] < s:
        b=l[i]
        for j in range(i-1,-1,-1):
            x[j+1]=x[j]
        x[0]=b
    for j in range(0, n):
        if x[j] == 0:
            # print(i)
            x[j] = s

# print(x)
for d in range(n):
    f=x[d]
    print(f,end=" ")
