from user import user_class
from user import super_user_class

print(
      "\n"
      "Hello Welcome to EdYoda Test Series\nDetails of test are given as follows \n "
      " Note:\n"
      "  1. This Test is MCQ Based\n"
      "  2. Select answer to proceed for Next Question\n"
      "  3. Every Question have ONE correct answer. \n\n"
      "Kindly Please Follow on screen instructions\n"
      )



"""
print('Let the system know you are:  \n 1. user\n 2. super_user\n')

key= input("Please Enter \n'SUPER USER KEY': To Authenticate You :\n"
           "If 'USER' , 'KEY' is  user \n")

if key=='super_user@123':
      print(" Welcome You Are Now 'super_user'")

if key =='user':
      print("Welcome You Are Now 'user': \nFeatures you can access\n\n"
            
            "1. Take Quiz than system will display result and 'correct answer' with options\n"
            "2. Retake Quiz than system will display result and 'correct answer' with optipns\n"
            "You can select Quiz on the bases of: \n #Type# \n #Hardness# \n To select type and hardness follow on screen instructions\n")

      user1 = user_class('Vipin', 7500574058, 'kumar.vipin1v00@gmail.com')

      # ask user type of test
      question_type = user1.question_type()

      # ask user hardness of quiz
      question_hardness = user1.question_hardness()

      '''
      # print("test_case_que_type",question_type)
      # print('test_case_que hardness',question_hardness)
      '''

      take_retake = user_class.take_quiz_or_retake_quiz(user1, question_type, question_hardness)


else:
      print("Try with Correct Credentials")

"""



"""
user1 = user_class('Vipin',7500574058,'kumar.vipin1v00@gmail.com')

# ask user type of test
question_type= user1.question_type()

# ask user hardness of quiz
question_hardness = user1.question_hardness()

'''
# print("test_case_que_type",question_type)
# print('test_case_que hardness',question_hardness)
'''

take_retake= user_class.take_quiz_or_retake_quiz(user1,question_type,question_hardness)


"""




"""
print(
      "Please Enter details :\n"
      " 1. Your Name :\n"
      " 2. Your Email :\n"
      " 3. Your Phone No. :\n"
      )

print(
      '''Hurray! You have entered details:\n
Mention Topic you want to take Quiz. :\n 1. "str"\n 2. "list"\n 3. "loop"\n 4. "fucn"\n 5. "dict"\n\nSelect options 1,2,3,4,5\n  
Mention Hardness of question  :\n 1. "Easy"\n 2. "Medium"\n 3. "Hard :"\n\nSelect options 1,2,3
'''
       )
"""
