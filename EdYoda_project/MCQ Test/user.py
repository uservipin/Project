from quiz_feature import test



class super_user:

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

    def take_test(self):
        test.start_test(self)


    def retake_test(self):
        test.retake_quiz(self)
