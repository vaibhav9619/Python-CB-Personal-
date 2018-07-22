n = int(input())
l=list(map(int,input().split()))[:n]
# print(l)
s=l[n-1]
j = (-1)
for i in range(0,n):
    if l[i]<=s:
        j+=1
        temp = l[i]
        l[i] = l[j]
        l[j]=temp
q1=l[j+1]
l[j+1]=l[n-1]
l[n-1]=q1
# for i in range(n):
print(l)




