
from bookManagement import bookManagement
from billingLibraryBook import billingLibraryBook


class BookReserveReturn:

    def reserveBook (name, student_id,book_title,days):
        for book in bookManagement.book_list:
            if book.title == book_title and len(book.book_item) != 0:
                book_item = book.book_item.pop()
                book.total_count -= 1
                bookManagement.updateIssuerInfo(book_item, name, student_id, days)
                bookManagement.addToReservedList(book_item)
                return book_item

            else:

                print("The book you're trying to reserve is unavailable.")



    def returnBook(ret_book_item, days):
        for book in bookManagement.book_list:
            if book == ret_book_item.book:
                book.book_item.append(ret_book_item)
                book.total_count +=1

        bookManagement.clearIssuesInfo(ret_book_item)
        bookManagement.removeFromReservedList(ret_book_item)
        billingLibraryBook.calculateBill(days)

    def extendDates(book_item,ext_days):
        bookManagement.extendDates(book_item,ext_days)





