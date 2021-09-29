from quiz_feature import test
from quiz import  quiz


class super_user_class:
    list_of_super_user= []

    @classmethod
    def add_super_user(cls,list_of_details_of_super_user):
        cls.list_of_super_user.append(list_of_details_of_super_user)

    def __init__(self,name,Email,PhoneNo):
        self.name= name
        self.Email= Email
        self.PhoneNo= PhoneNo
        super_user_class.add_super_user((self))

    def add_question_to_test(self):

        # print('type_of_que',que_type)
        # print('hardness',hardness)

        quiz_que1 = quiz()

        question_type = quiz_que1.type_of_question()
        hardn = quiz_que1.hardness_of_question()

        quiz_que1.update_question(1, 'What is even NO. : ', [1, 2, 3, 5], 2)
        que1 = quiz_que1.dict_of_question
        # print("que1", que1)
        quiz.add_question_to_mcq_list(self =que1 ,que_type=question_type,hardness=hardn)

    def update_question(self):

        quiz_que1 = quiz()
        question_type = quiz.type_of_question(self)
        hardn = quiz.hardness_of_question(self)

        quiz_que1.update_question(1, 'What is even NO. : ', [1, 2, 3, 5], 2)
        que1 = quiz_que1.dict_of_question
        quiz.add_question_to_mcq_list(self =que1 ,que_type=question_type,hardness=hardn)

    def delete_question_paper(self):
        question_type = quiz.type_of_question(self)
        hardn = quiz.hardness_of_question(self)
        quiz.remove_question_from_mcq_test(self,question_type,hardn)

    def set_multiple_quiz(self):
        pass

class user_class:
    user_list=[]
    @classmethod
    def add_user_list(cls,user):
        user_class.user_list.append(user)

    def __init__(self,name,Email,Phone_No):
        self.name= name
        self.Email= Email
        self.Phone_No= Phone_No
        user_class.add_user_list(self)

    # Here First ask type and level of question
    def take_test(self,question_type,question_hardness):
        test.start_test(self,question_type,question_hardness)

    def retake_test(self,question_type,question_hardness):
        test.retake_quiz(self,question_type,question_hardness)

    def question_type(self):
        question_type = quiz.type_of_question(self)
        return question_type

    def question_hardness(self):
        hardness = quiz.hardness_of_question(self)
        return hardness

    def take_quiz_or_retake_quiz(self,question_type,question_hardness):
        input_var= int(input("\n Enter: 1  For Take Quiz\n Enter: 2  For Retake Quiz\n"))

        if input_var == 1:
            user_class.take_test(self,question_type,question_hardness)

        if input_var == 2:
            user_class.retake_test(self,question_type,question_hardness)

