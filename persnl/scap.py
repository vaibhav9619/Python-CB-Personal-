s=input()
l=list(s)
for i in range(1,len(l)-1):
    if l[i-1] == 'a' or l[i-1] == 'e' or l[i-1] == 'i' or l[i-1] == 'o' or l[i-1] == 'u':
        if l[i+1] == 'a' or l[i+1] == 'e' or l[i+1] == 'i' or l[i+1] == 'o' or l[i+1] == 'u':
            print(l[i],end="")
    else:
        print("-1")
        break