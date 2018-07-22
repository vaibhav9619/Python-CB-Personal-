file = open("abc.txt")
# a=file.read(4)#print 4 character from that file read file by char count
# print(a)
# a=file.read(100)#print 4 character from that file read the file
# print(a) #print next 4 character rather than same
#  helps to cruch the file it lowers the mem wastage


# a=file.read()# memeory wastage no parameter declared it ill display the whole file
# print(a)


# a=file.readline()#read by line
# b=file.readline()#read by line
# print(a,b)

for i in file:
    print(i,end="")
# if we apply for loop agin it will not print again
#once file is read it will not go back
# w=write
# r=read
# a=append
# x=create