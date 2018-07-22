from peewee import SqliteDatabase, Model  # model tells the architecture
from peewee import CharField,PrimaryKeyField

db = SqliteDatabase("library.db")
class Base(Model):
    class Meta:
        database=db# object provide of class Sqlite

class User(Base):
    id=PrimaryKeyField()#only once
    # id = CharFi?eld()  # tell us about char field of limited size (nearly 60 char)
    password = CharField()



class Book(Base):
    id=PrimaryKeyField()#only once
    name = CharField()  # tell us about char field of limited size (nearly 60 char)
    author = CharField()




db.connect()
# db.create_tables([Book])
db.create_tables([Book,User])
# myBook = Book.create(id=1,name="Azkabaan ka kaidi", author="JkrR")
# # yourBook = Book.create(id=2,name="hello moto", author="vaibhav")
# # pyBook = Book.create(id=3,name=" kaidi", author="khan prod")

# b1 = Book(id=1,name="Azkabaan ka kaidi", author="JkrR")
# b2 = Book(id=2,name="hello moto", author="vaibhav")
# b3 = Book(id=3,name=" kaidi", author="khan prod")
# b1.save()
# b2.save()
# b3.save()
#
#
# books = Book.select()
# for book in books:
#     print(book.author, " --", book.name)
def create(id,password):
    try:
        bla=User.create(id=id,password=password)
    except:
        print("Already exist")
anuj=create(14,"baby")
ms=create(134,"doll")
# anuj=User(id=1234,password="alpha")
users=User.select()
for i in users:
    print(i.id,i.password)
