""":cvar

addReservedBooks
updateIssuerInfo
add to reserved list
remove from reserved list
clear issuer informationextend datetime
"""


class BookItem:

    reserved_book_list=[]

    @classmethod
    def addReservedBooks(cls,book):
        cls.BookItem.reserved_book_list.append(book)

    def __init__(self,book,isbn,rack):
        self.book= book
        self.isbn= isbn
        self.rack= rack
        self.info= {}

    def updateIssuerInfo(self,name,student_ID,days):
        self.info["Name"] = name
        self.student_ID= student_ID
        self.days= days

    def ToReservedList(self):
        BookItem.addReservedBooks(self)

    def removeFromReservedList(self):
        BookItem.reserved_book_list.remove(self)

    def claeIssuerInfo(self):
        self.info.clear()


    def extenDates(self,ext_days):
        if self.info['Days'] + ext_days <=15:
            self.info["days"]= self.info["days"]+ ext_days
            print(f"{ext_days} days extended successfully for {self.isbn}")
        else:
            print("Days can't be extended")



        
