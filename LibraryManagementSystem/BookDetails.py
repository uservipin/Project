"""
List of method used in this class

"""


class BookDetails:

    # list to store details of books
    booksArchive = []
    @classmethod
    def addBookArchive(cls,book):
        cls.booksArchive.append(book)

    def __init__(self,book,isbn,rack_in_lib):
        self.book= book
        self.isbn= isbn
        self.rack_in_lib=rack_in_lib
        self.info= {}

    def updateIssuerInfo(self,name,studentId,days):
        self.info["name"]=name
        self.info["Student Id"]= studentId
        self.info["days"]= days
        return self.info

    def addToBookArchive(self):
        BookDetails.addBookArchive(self)

    def removeFromBookArchiveList(self):
        BookDetails.booksArchive.remove(self)

    def clearIssuerInfo(self):
        self.info.clear()

    def extendDates(self,ext_days):
        if self.info["Days"] + ext_days <= 10:
            self.info["Days"] = self.info["Days"] + ext_days
            print("{} days extended successfully for {}".format(ext_days, self.isbn))
        else:
            print("Days cannot be extended over allowed maximum days.")






# book_details =BookDetails('start with why','1234544344','5')
# book_details2 =BookDetails('start with why','1234544344','5')
#
#
#
# book_details2.addBookArchive("test")
# book_details2.addBookArchive("test01")
# book_details2.addBookArchive("test02")
#
# print(book_details2.booksArchive)
#
# BookDetails.removeFromBookArchiveList('test02')
#
# print(book_details2.booksArchive)
#
#
#
# print(book_details2 .clearIssuerInfo())
#
#

