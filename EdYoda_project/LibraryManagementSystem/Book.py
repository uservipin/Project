from Questions import BookItem

class Book:


    def __init__(self,title, author,catagory,publication_date):
        self.title= title
        self.author= author
        self.catagory= catagory
        self.public_date= publication_date
        self.total_count=0
        self.book_item =[]

    def addBookItem(self,isbn,rack):
        b= BookItem(self,isbn,rack)
        self.book_item.append(b)
        self.total_count += 1

    def printBook(self):
        print("{} by {} ".format(self.title,self.author))

        for book_item in self.book_item:
            print("Isbn : {} , racn : {}". format(book_item.isbn,book_item.rack))


    def viewReservedBookItems():
        if len(BookItem.reserved_book_list)>=1:
            for item in Book.reserved_book_list:
                print(item.isbn)

            else:
                print("No book are reserved at this moment")

    def viewIssuerInfo(isbn):
        for book_item in BookItem.reserved_books:
            if book_item.isbn == isbn:

                print("issueed by :" +book_item.info.info["Name"])
                print("Student ID:"+ book_item.info["Student_ID"])
                print("Issued for:" + str(book_item.info.info["Days"]) + "days")



    def updateIssuerInfo(book_item,name,student_id,days):
        BookItem.updateIssuerInfo(book_item,name,student_id,days)

    def addToReservedList(book_item):
        BookItem.addToReservedList(book_item)

    def clearIssuerInfo(ret_book_item):
        BookItem.clearToReservedList(ret_book_item)

    def removeFromReservedList(ret_book_item):
        BookItem.removeFromReservedList(ret_book_item)



