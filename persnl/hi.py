n=int(input())
l=[]
for i in range(n):
    s=int(input())
    l.append(s)

l.sort()

line = ("\n").join(map(str, l))

print(line)

