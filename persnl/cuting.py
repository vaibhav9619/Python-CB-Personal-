n=int(input())
c=0
c1=0
li=[]
li=list(map(int,input().split()))
for i in range(0,len(li)):
    if(li[i]>0):
        c+=1;
# print(c)
# print(li)
# s=min(li)
# print(s)
for j in range(len(li)):
    c1=0
    s=list(filter(lambda a : a>0,li))
    p=min(s)
    for i in range(len(li)):
        if li[i] > 0 :
            li[i]=li[i]-p
            c1+=1
    # list(filter(lambda a: a>0,li))
    print(c1)
    # print(li)

