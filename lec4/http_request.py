
from urllib import request #from package import module
#when used onlt request is used rather than all
data=request.urlopen("https://www.google.com/")
# data=request.urlopen("https://www.google.com/jwbhgisdfdfkjffas")#unknown page error 404
print(data.read()) #displays the html code  of google
print(type(data))#display
print(data.version)
print(data.status)
#200 erroe-ok
# 404 page not found/not found
# 500 internal server error