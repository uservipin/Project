from quiz_feature import test
from quiz import  quiz


class super_user_class:

    def __init__(self):
        pass
    def set_hardness_of_test(self):
        pass

    def set_level_of_test(self):
        pass

    def update_question(self):
        pass

    def delete_question_paper(self):
        pass

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

