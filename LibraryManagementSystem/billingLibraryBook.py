
#nvbnv
class billingLibraryBook:

    def calculateBill(days):
        max_days =15
        per_day_fine= 50

        if days > max_days:
            fine_days = days- max_days
            fine = fine_days*per_day_fine
            print(" Fine for Extra days {},  and amount {} Rs.".format(fine_days, fine))

        else:
            print("Thank you for returning book on time!")