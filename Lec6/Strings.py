#empty string has default value False
# else value is true(if string contain saome value)
str=["sf","","sfdusd"]
str=list(map(lambda x: bool(x),str))
print(str)