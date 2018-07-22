from functools import reduce
li=[213,24,577,879]
# reduce has 3 parameters reduce(function,sequence,inital=None)
# s=reduce(lambda x,y : x+y ,li,0)#for multiply initail value is 1
#
s=reduce(lambda x,y : print(y) ,li,0)#initial value of print(x) = 0 so it displays hen print(y) displays all the value of x then print none NoNe
print(s)
#
# s1=reduce(lambda x,y : print(x) ,li,0)#print return none so it initailly make prit(x) =none so all value shows none
# print(s1)

# print by default returns NONE
s=reduce(lambda x,y : print(x) ,li,0)
print(s)