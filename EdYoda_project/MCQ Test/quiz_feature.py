"""
Note Run "test_case.py"  file and follow On screen instructions
"""

from quiz import quiz

# get basic detail of user
class test:
    # global(marks_per_question )= 4

    def __init__(self,User_Name, User_Phone_No, User_Email_Id):

        self.User_Name = User_Name
        self.User_Phone_No = User_Phone_No
        self.User_Email_Id = User_Email_Id

    def start_test(self,question_type,question_hardness):

        '''
        print('quiz_feature_que_type',question_type)
        print('quiz_feature_quiz_hardness',question_hardness)

        :param question_type:
        :param question_hardness:
        :return:
        '''
        print("\nAnswer the questons: ")
        list_of_que = quiz.Mcq_List[0][question_type][question_hardness]
        score = 0
        for questions in list_of_que:
            # print(questions)
            print('\n',questions['question'])
            # print("Please select any one option")
            print("Options are :", questions['options'], '\n Select\n 1 : For First\n 2 : For Second\n 3 : For Third\n 4 : For Fourth')
            # print("answer :", type(questions['correct_answer']))
            answer = int(input("Enter: 'Answer' in int  1  2  3  4  "))
            # print('\n')
            if answer == questions['correct_answer']:
                score += 1
        print("\nYour score is: ", score, "out of", len(list_of_que),'\n')

        right_answers_are = test.display_write_answer(self,question_type,question_hardness)
        # print(right_answers_are)

    def retake_quiz(self,question_type,question_hardness):

        print("\nAnswer the questons: ")
        list_of_que = quiz.Mcq_List[0][question_type][question_hardness]
        score = 0
        for questions in list_of_que:
            # print(questions)
            print('\n',questions['question'])
            # print("Please select any one option")
            print("Options are :", questions['options'], '\n Select\n 1 : For First\n 2 : For Second\n 3 : For Third\n 4 : For Fourth')
            # print("answer :", type(questions['correct_answer']))
            answer = int(input("Enter: 'Answer' in int  1  2  3  4  "))
            # print('\n')
            if answer == questions['correct_answer']:
                score += 1
        print("\nYour Retake score is : ", score, "out of", len(list_of_que))

        right_answers_are = test.display_write_answer(self,question_type,question_hardness)
        # print(right_answers_are)

    def display_write_answer(self,question_type,question_hardness):
        list_of_que = quiz.Mcq_List[0][question_type][question_hardness]

        print('Correct Answers are: ')
        for questions in list_of_que:
            # print('\n\n\n',questions,'\n\n\n')
            # questions['correct_answer']
            # print('\n',questions['question'], '\nOptions are: ',questions['options'],  '\nCorrect Answer is: ',questions['options'][questions['correct_answer']-1])
            print('\n',questions['question'], '\nOptions are: ',questions['options'],  '\nCorrect Answer is: ',questions['correct_answer'])


