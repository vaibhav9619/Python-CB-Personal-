n=int(input())
d={}
x={}
l=[]
for i in range(n):
    n=input()
    p=int(input())
    d[n]=p
    e=input()
    l.append(e)
print(d)
print(l)
for i in range(len(l)):
    for k,v in d.items():
        if l[i] == k:
            d[k]=v
            break
print(d)


# print(d)

# s=dict(map())

