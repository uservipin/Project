from quiz import quiz

# get basic detail of user
class test:
    # global(marks_per_question )= 4

    def __init__(self,User_Name, User_Phone_No, User_Email_Id):

        self.User_Name = User_Name
        self.User_Phone_No = User_Phone_No
        self.User_Email_Id = User_Email_Id


    def start_test(self):
        list_of_que= quiz.Mcq_List

        score = 0
        for questions in list_of_que:
            # print(questions)
            print(questions['question'])
            # print("Please select any one option")
            print("Please select any one option from list : ", questions['options'], '1: For First ', ' ', '2 For Second ', ' ', '3 For third ',' ','4 for Forth option')
            # print("answer :", type(questions['correct_answer']))
            answer = int(input("Please ans this question"))
            print('\n')
            if answer == questions['correct_answer']:
                score += 1
        print("you got", score, "out of", len(list_of_que))

    def retake_quiz(self):
        list_of_que = quiz.Mcq_List

        score = 0
        for questions in list_of_que:
            # print(questions)
            print(questions['question'])
            # print("Please select any one option")
            print("Please select any one option from list : ", questions['options'], '1: For First ', ' ', '2 For Second ', ' ',
                  '3 For third ', ' ', '4 for Forth option')
            # print("answer :", type(questions['correct_answer']))
            answer = int(input("Please ans this question"))
            print('\n')
            if answer == questions['correct_answer']:
                score += 1
        print("Your Retake score is : ", score, "out of", len(list_of_que))

    def display_write_answer(self):
        list_of_que = quiz.Mcq_List

        for questions in list_of_que:
            # print(questions)
            questions['correct_answer']
            print(questions['question'], 'Options are ',questions['options'],  'correct answer is ',questions['options'][questions['correct_answer']-1])













Maths_test = test('Vipin',7500574058,'kumar.vipin1v00@gmail.com')

# test1.start_test()

# Maths_test.retake_quiz()
print(Maths_test.User_Name)
print(Maths_test.User_Phone_No)
print(Maths_test.User_Email_Id)

Maths_test.display_write_answer()

