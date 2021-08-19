from Book import Book

class Catalog:

    book_list=[]
    different_book_count=0

    @classmethod
    def addBookList(cls,book):
        cls.book_list.append(book)


    def addBook(title, author,catagory,publication_date):
        b= Book(title,author,catagory,publication_date)
        Catalog.book_list.append(b)
        Catalog.different_book_count +=1

    def addBookItem(title,isbn,rack):
        for book in Catalog.book_list:
            if book.title == title:
                b= Book.addBookItem(book,isbn,rack)
                print("BOOK iTEM {} has been added successfully !", format(isbn))


    def removeBook(rem_book):
        for book in Catalog.book_list:
            if book.title == rem_book:
                Catalog.book_list.remove(book)
                Catalog.different_book_count -= 1
                print("Book Ite {} has been addes successfully added !".format(rem_book))

    def removeBookItem(rem_bookItem):

        for book in Catalog.book_list:
            for book_Item in book.book_item:
                if book_Item.isbn == rem_bookItem:
                    book.book_item.remove(book_Item)
                    book.total_count -=1
                    print("Book Item {} has been removed from the catalog !".foormat(rem_bookItem))

    def searchByTitle(title):
        for book in Catalog.book_list:
            if book.title == title:
                print("Book Available")
                break

            else:
                print("Sorry .. no books are available by this title")


    def searchByAuthor(author):

        count = 0

        for book in Catalog.book_list:
            if book.author == author:
                print(book.title)
                count +=1

            if count ==0:
                print("Sorry .. No books are available by author")


    def searchByCatagory(catagory):

        count = 0

        for book in Catalog.book_list:
            if book.category==catagory:
                print(book.catagory)
                count +=1

            if count ==0:
                print("Sorry .. No books are available by this catagory")


    def searchByPublicationDate(publication_date):
        count = 0

        for book in Catalog.book_list:
            if book.public_date== publication_date:
                print(book.publication_date)
                count +=1

            if count ==0:
                print("Sorry .. No books are available by publication date")



    def displayAllBooks():
        c=0
        for book in Catalog.book_list:
            c += book.total_count
            book.printBook()
            print("DIfferent book count ", Catalog.different_book_count)
            print("total book count",c)

    def updateIssuerInfo(book_item,name,student_id,days):
        Book.updateIssuerInfo(book_item, name, student_id, days)

    def addToReservedList(book_item):
        Book.addToReservedList(book_item)

    def clearIssuerInfo(ret_book_item):
        Book.clearIssuerInfo(ret_book_item)

    def removeToReservedList(ret_book_item):
        Book.removeFromReservedList(ret_book_item)

    def extend_dates(book_item,extend_date):
        Book.extendDates(book_item,extend_date)

    def viewReservedBookItem():
        Book.viewReservedBookItem()

    def viewIssuerInfo(isbn):
        Book.issuerInfo(isbn)





