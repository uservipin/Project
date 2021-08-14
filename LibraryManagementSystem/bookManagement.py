

from bookBank import bookBank

class bookManagement:
    book_list=[]
    diff_book_counter = 0

    @classmethod
    def addBookList(cls,book):
        cls.book_list.append(book)

    def addBook(title, author, category, publication_date):
        b = bookBank(title, author, category, publication_date)
        bookManagement.addBooksList(b)
        bookManagement.different_book_count += 1
        print("Book {} has been added successfully!".format(title))

    def addBookItem(title,isbn,rack):
        for book in bookManagement.book_list:
            if book.title == title:
                b= bookBank.addBookItem(book, isbn, rack)
                print("Book item {} has been added successfully :",format(isbn))

    def removeBook(rem_book):
        for book in bookManagement.book_list:
            if book.title == rem_book:
                bookManagement.different_book_count -=1
                print("Book {} has been removed from the book management ".format(rem_book))

    def removeBookItem(rem_bookitem):
        for book in bookManagement.book_list:
            for book_item in book.bookItem:
                if book_item.isbn == rem_bookitem:
                    book.bookItem.remove(book_item)
                    book.total_count -= 1
                    print("Book Item {} has been removed from the catalog!".format(rem_bookitem))




    def searchByTitle(title):
        for book in bookManagement.book_list:
            if book.title == title:
                print('Bool available')

            else:
                print('We are sorry: No book availabele')

    def searchByAuthor(author):
        count =0
        for book in bookManagement:
            if book.author== author:
                print(book.title)
                count +=1
            if count ==0:
                print(" We are Sorry.. no books are available by this author! Please try again after sometime")


    def searchByCategory(category):
        count = 0
        for book in bookManagement.bookList:
            if book.bookManagement == category:
                print(book.title)
                count += 1
        if count == 0:
            print("Sorry.. no books are available under this category")

    def searchByPublicationData(publicationData):
        count = 0
        for book in bookManagement.bookList:
            if book.publicationData == publicationData:
                print(book.title)
                count +=1

            if count ==0:
                print( "No book are availabel by this publisher")

    def displayAllBooks ():
        c=0
        for book in bookManagement.book_list:
            c +=book.total_count
            book.printBook()
            print("Different Book Count", bookManagement.different_book_count)
            print("Total Book Count", c)

    def updateIssueInfo(book_items,name,student_id,days):
        bookBank.updateIssuerInfo(book_items,name,student_id,days)

    def addToReservedList(book_item):
        bookBank.addToReservedList(book_item)

    def clearIssuesInfo(ret_book_item):
        bookBank.clearIssuerInfo(ret_book_item)

    def removeFromReservedList(ret_book_item):
        bookBank.removeFromReservedList(ret_book_item)

    def extendDates(book_item,ext_days):
        bookBank.extendDates(book_item, ext_days)

    def viewReservedBookItem():
        bookBank.viewReservedBookItem()

    def viewIssueInfo(isbn):
        bookBank.viewReservedBookItem(isbn)

