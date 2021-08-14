
from BookDetails import BookDetails



class bookBank:

    def __init__(self,title,author, category,publication_date):
        self.title = title
        self.author = author
        self.category = category
        self.publication_date = publication_date
        self.total_count = 0
        self.book_item = []

    def addBookItem(self,isbn,rack_in_lib):
        b= BookDetails(self,isbn,rack_in_lib)
        self.book_item.append(b)
        self.total_count += 1
        
    def printBookDetail(self):
        print("{} by {}".format(self.title,self.author))
        for book_item in self.book_item:
            print("Isbn : {} , Rack: {}". format(book_item.isbn, book_item.rack_in_lib))

    def viewReservedBookItem():
        if len(BookDetails.booksArchive) >=1:
            for item in BookDetails.booksArchive:
                print(item.isbn)
        else:
            print(" No book are reserved at this moment")

    def viewIssuerInfo(isbn):

        for book_item in BookDetails.booksArchive:
            if book_item.isbn == isbn:
                print("Issued by :" + book_item.info["Name"])
                print("Student Id : " + book_item.info["Student Id"])
                print("issuer for :"+ str(book_item.info["Days"])+ "days")

    def updateIssuerInfo(book_item,name, student_id,days):
        BookDetails.updateIssuerInfo(book_item,name,student_id,days)

    def addToBookAerchive(book_item):
        BookDetails.addBookArchive(book_item)

    def clearIssuerInfo(ret_book_item):
        BookDetails.clearIssuerInfo()

    def removeFromReservedList(ret_book_item):
        BookDetails.removeFromBookArchiveList(ret_book_item)

    def extendDates(book_item, ext_days):
        BookDetails.extendDates(book_item,ext_days)

bookBank1 = bookBank("Atomic habbit","jack sparrow","educational",2015)
bookBank2= bookBank("Start with why", "simon sinek", "business",2005)

bookBank1.addBookItem(12344545445444-3,5)

print("Book details are:",bookBank1.printBookDetail())

print("Reserved books are: ",bookBank.viewReservedBookItem())

print("Issuer is : ",bookBank.viewIssuerInfo(12344545445444-3))