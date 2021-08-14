# import classes

from bookReserveReturn import BookReserveReturn

from bookManagement import bookManagement

class user:
    def __init__(self,name, location, age,aadhar_id):
        self.name= name
        self.location= location
        self.age = age
        self.aadhar_id =aadhar_id

    def viewBooks(self):
        bookManagement.displayAllBooks()

class Librarian(user):

    def __init__(self,name,location,age, aadhar_id ,employee_id ):
        super().__init__(name,location,age,aadhar_id)
        self.employee_id= employee_id

    def __repr__(self):
        return self.name + " " +  self.location + " " + self.employee_id

    def addBook(self, title,author,category,publication_data):
        bookManagement.addBook(title,author,category,publication_data)

    def addBookItem(self , title, isbn,rack):
        bookManagement.addBookItem(title, isbn, rack)

    def removeBook(self, rem_book):
        bookManagement.removeBook(rem_book)

    def removeBookItem(self,rem_bookitem):
        bookManagement.removeBook(rem_bookitem)

    def addMenber(self, name, location, age, aadhar_id, student_id):
        Member(name, location, age, aadhar_id, student_id)

    def removeMember(self,name):
        for member in Member.members_list:
            if menber.name == name:
                Member.members_list.remove(member)
                print(" {} was successfully removed from library!".format(name))
                break

            else:
                print("No menber exist by this name")

    def viewMenbers(self,name):
        for member in Member.members_list:
            print(member)

    def searchMember(self,name):
        for member in Member.members_list:
            if member.name == name:
                print(member)
                for book_item in member.issued_books_list:
                    print(book_item.book.title, book_item.isbn)
                break
        else:
            print("There are no registered members in this library by this name.")

    def viewReservedBookItems(self):
        bookManagement.viewReservedBookItem()

    def viewIssueInfo(self):
        isbn = input( "Please enter isbn of the book for which you'd like to view issuer information for: ")
        bookManagement.viewIssueInfo()


class Member(user):
    members_List= []

    @classmethod
    def addMemberList(cls,member):
        cls.members_List.append(member)


    def __init__(self,name, location, age, aadhar_id,student_id):
        super().__init__(name,location,age,aadhar_id)
        self.student_id= student_id
        self.issued_book_list= []
        Member.addMemberList(self)

        print("Welcome to Library Members{}".format(name))

    def __repr__(self):
        return self.name + " " + self.location + " " + self.student_id

    def searchByTitle(self, title):
        bookManagement.searchByTitle(title)

    def searchByAuthor(self, author):
        bookManagement.searchByAuthor(author)

    def searchByCategory(self, category):
        bookManagement.searchByCategory(category)

    def searchByPublicationDate(self, publication_date):
        bookManagement.searchByPublicationDate(publication_date)




    def extendDates(self):
        print("BOOKS CURRENTLY ISSUED BY YOU: ")
        for book_item in self.issued_books_list:
            print(book_item.isbn)
        isbn = input("Please enter isbn of the book for which you'd like to extend dates: ")
        ext_days = int(input("Please enter the number of days you'd like to extend for: "))
        for book_item in self.issued_books_list:
            if book_item.isbn == isbn:
                bookReserveReturn.extendDates(book_item, ext_days)



    def returnBook(self):
        print("BOOKS CURRENTLY ISSUED BY YOU: ")
        for book_item in self.issued_books_list:
            print(book_item.book.title, book_item.isbn)
        isbn = input("Which book would you like to return? Enter isbn: ")
        days = int(input("How many days has it been since you issued this book? Be honest! "))
        for book_item in self.issued_books_list:
            if book_item.isbn == isbn:
                ret_book_item = book_item
            else:
                print("Sorry.. the book you're trying to return is not issued by you!")
        bookReserveReturn.returnBook(ret_book_item, days)
        self.issued_books_list.remove(ret_book_item)

    def reserveBook(self, book_title):
        days = 0
        max_days = 10
        condition1 = [False, "Sorry.. your membership has been revoked.\nContact librarian for further details."]
        for member in Member.members_list:
            if member == self:
                condition1[0] = True
                days = int(input("For how many days would you like to issue this book? "))

        condition2 = [False, "Sorry! You can issue a book for a maximum of {} days".format(max_days)]
        if days <= max_days:
            condition2[0] = True

        condition3 = [False, "You can issue a maximum of 5 books at a time"]
        if len(member.issued_books_list) < 5:
            condition3[0] = True

        conditions = [condition1, condition2, condition3]

        for condition in conditions:
            if condition[0] == False:
                print(condition[1])
                break
        else:
            book_item = bookReserveReturn.reserveBook(self.name, self.student_id, book_title, days)
            self.issued_books_list.append(book_item)
            print("Book reserved successfully!")
            print("Grab your copy {} from rack {}".format(book_item.isbn, book_item.rack))


























