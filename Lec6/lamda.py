def sq(num):
    return num*num
# print(s(21))
l=[21,23,125,412]
# s1=list(map(sq,l)) without lambda
s1=list(map(lambda x:x*x,l))
print(s1)
big=list(filter(lambda y:y>100,l)) #remove all items less than 100
print(big)