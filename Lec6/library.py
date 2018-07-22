class library:
    def __init__(self):
        self.books=list()
    def __repr__(self):#for representation Print meaning full data
        return str(self.books)
class Book:
    def __init__(self, name, author, price):
        self.name=name
        self.author=author
        self.price=price
    def __repr__(self):
        return str([self.name,self.author,self.price])
lib=library()
if __name__=='__main__':
    b=Book("Maluha","vaibhav",200)
    b1=Book("harryPottter","sadana",250)
    b2 = Book("Fault", "sam", 100)
    b3 = Book("kaidi", "sanju", 1250)
# b=Book("Maluha","vaibhav",200)
# b1=Book("harryPottter","sadana",250)
# b2 = Book("Fault", "sam", 100)
# b3 = Book("kaidi", "sanju", 1250)

lib.books+=[b,b1,b2,b3]
s=list(filter (lambda item:item.price>200,lib.books)) #filter all the books
s1=list(filter(lambda item:item.author=="sam",lib.books))
print(lib)
print(s)
print(s1)