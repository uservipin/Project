class quiz:

    dict_srt= {
    'Easy':[
            {'id':1, 'question' :'What arithmetic operators cannot be used with strings?','options': 'a) + b) *c) – d) All of the mentionedc','correct_answer': 4},
            {'id':2, 'question' :"""What will be the output of the following Python statement? '\n' >>>print("a"+"bc") """ ,'options': '1) a 2) bc 3) bca 4) abc','correct_answer': 4},
            {'id':3, 'question' :"""What will be the output of the following Python statement? '\n' >>>print("abcd"[2:]) """ ,'options': 'a) a  b) ab c) cd d) dc','correct_answer': 3},
            {'id':4, 'question' :"""What will be the output of the following Python statement? '\n' >>>print(r"\nhello") """ ,'options': ' a) a new line and hello  b) \nhello  c) the letter r and then hello  d) error ','correct_answer': 4},
            {'id':5, 'question' :"""What will be the output of the following Python statement? '\n' "a"+"bc" """ ,'options': '1) a 2) bc 3) bca 4) abc','correct_answer': 2}
            ],
    'Medium':[
            {'id': 1, 'question': """What will be the output of the following Python statement? '\n'print('abcd'.translate({97: 98, 98: 99, 99: 100})) """, 'options': ' a) bcde b) abcd c) error  d) none of the mentioned ', 'correct_answer': 4},
            {'id': 2, 'question': """What will be the output of the following Python statement? '\n'print('abcdefcdghcd'.split('cd', 2)) """, 'options': ' a) [‘ab’, ‘ef’, ‘ghcd’] b) [‘ab’, ‘efcdghcd’] c) [‘abcdef’, ‘ghcd’] d) none of the mentioned ', 'correct_answer': 1},
            {'id': 3, 'question': """What will be the output of the following Python statement? '\n' print('ab\ncd\nef'.splitlines())  """, 'options': ' a) [‘ab’, ‘cd’, ‘ef’] b) [‘ab\n’, ‘cd\n’, ‘ef\n’]  c) [‘ab\n’, ‘cd\n’, ‘ef’]  d) [‘ab’, ‘cd’, ‘ef\n’] ', 'correct_answer': 1},
            {'id': 4, 'question': """What will be the output of the following Python statement? '\n' >>>print(r"\nhello") """, 'options': ' a) AB!@ b) ab12 c) aB!2  d) aB1@ ',  'correct_answer': 3},
            {'id': 5, 'question': """What will be the output of the following Python statement? '\n' print('ab cd ef'.title()) """, 'options': ' a) Ab cd ef b) Ab cd eF  c) Ab Cd Ef  d) None of the mentioned ', 'correct_answer': 3}
            ],
    'Hard': [
            {'id': 1,  'question': """What will be the output of the following Python statement? '\n  print('abcd'.translate({'a': '1', 'b': '2', 'c': '3', 'd': '4'}))  """,  'options': ' a) abcd b) 1234  c) error d) none of the mentioned ', 'correct_answer': 1},
            {'id': 2,  'question': """What will be the output of the following Python statement? '\n'print('ab'.zfill(5))""",   'options': ' a) 000ab  b) 00ab0 c) 0ab00 d) ab000 ',   'correct_answer': 1},
            {'id': 3, 'question': """What will be the output of the following Python statement? '\n' print('+99'.zfill(5))   """, 'options': ' a) [‘ab’, ‘cd’, ‘ef’] b) [‘ab\n’, ‘cd\n’, ‘ef\n’]  c) [‘ab\n’, ‘cd\n’, ‘ef’]  d) [‘ab’, ‘cd’, ‘ef\n’] ', 'correct_answer': 1},
            {'id': 4, 'question': """What will be the output of the following Python statement? '\n' >>>print(r"\nhello") """, 'options': ' a) 00+99 b) 0009 c) +0099  d) +++99 ', 'correct_answer': 3},
            {'id': 5,  'question': """What will be the output of the following Python statement? '\n' print(max("what are you")) """, 'options': ' a) error  b) u c) t  d) y   ', 'correct_answer': 4}
          ]
        }

    dict_list={
    'Easy': [
      {'id': 1, 'question': 'What arithmetic operators cannot be used with strings?',
       'options': 'a) + b) *c) – d) All of the mentionedc', 'correct_answer': 4},
      {'id': 2, 'question': """What will be the output of the following Python statement? '\n' >>>print("a"+"bc") """,
       'options': '1) a 2) bc 3) bca 4) abc', 'correct_answer': 4},
      {'id': 3, 'question': """What will be the output of the following Python statement? '\n' >>>print("abcd"[2:]) """,
       'options': 'a) a  b) ab c) cd d) dc', 'correct_answer': 3},
      {'id': 4, 'question': """What will be the output of the following Python statement? '\n' >>>print(r"\nhello") """,
       'options': ' a) a new line and hello  b) \nhello  c) the letter r and then hello  d) error ',
       'correct_answer': 4},
      {'id': 5, 'question': """What will be the output of the following Python statement? '\n' "a"+"bc" """,
       'options': '1) a 2) bc 3) bca 4) abc', 'correct_answer': 2}
    ],
    'Medium': [
      {'id': 1,
       'question': """What will be the output of the following Python statement? '\n'print('abcd'.translate({97: 98, 98: 99, 99: 100})) """,
       'options': ' a) bcde b) abcd c) error  d) none of the mentioned ', 'correct_answer': 4},
      {'id': 2,
       'question': """What will be the output of the following Python statement? '\n'print('abcdefcdghcd'.split('cd', 2)) """,
       'options': ' a) [‘ab’, ‘ef’, ‘ghcd’] b) [‘ab’, ‘efcdghcd’] c) [‘abcdef’, ‘ghcd’] d) none of the mentioned ',
       'correct_answer': 1},
      {'id': 3,
       'question': """What will be the output of the following Python statement? '\n' print('ab\ncd\nef'.splitlines())  """,
       'options': ' a) [‘ab’, ‘cd’, ‘ef’] b) [‘ab\n’, ‘cd\n’, ‘ef\n’]  c) [‘ab\n’, ‘cd\n’, ‘ef’]  d) [‘ab’, ‘cd’, ‘ef\n’] ',
       'correct_answer': 1},
      {'id': 4, 'question': """What will be the output of the following Python statement? '\n' >>>print(r"\nhello") """,
       'options': ' a) AB!@ b) ab12 c) aB!2  d) aB1@ ', 'correct_answer': 3},
      {'id': 5,
       'question': """What will be the output of the following Python statement? '\n' print('ab cd ef'.title()) """,
       'options': ' a) Ab cd ef b) Ab cd eF  c) Ab Cd Ef  d) None of the mentioned ', 'correct_answer': 3}
    ],
    'Hard': [
      {'id': 1,
       'question': """What will be the output of the following Python statement? '\n  print('abcd'.translate({'a': '1', 'b': '2', 'c': '3', 'd': '4'}))  """,
       'options': ' a) abcd b) 1234  c) error d) none of the mentioned ', 'correct_answer': 1},
      {'id': 2, 'question': """What will be the output of the following Python statement? '\n'print('ab'.zfill(5))""",
       'options': ' a) 000ab  b) 00ab0 c) 0ab00 d) ab000 ', 'correct_answer': 1},
      {'id': 3,
       'question': """What will be the output of the following Python statement? '\n' print('+99'.zfill(5))   """,
       'options': ' a) [‘ab’, ‘cd’, ‘ef’] b) [‘ab\n’, ‘cd\n’, ‘ef\n’]  c) [‘ab\n’, ‘cd\n’, ‘ef’]  d) [‘ab’, ‘cd’, ‘ef\n’] ',
       'correct_answer': 1},
      {'id': 4, 'question': """What will be the output of the following Python statement? '\n' >>>print(r"\nhello") """,
       'options': ' a) 00+99 b) 0009 c) +0099  d) +++99 ', 'correct_answer': 3},
      {'id': 5,
       'question': """What will be the output of the following Python statement? '\n' print(max("what are you")) """,
       'options': ' a) error  b) u c) t  d) y   ', 'correct_answer': 4}
    ]
    }

    dict_loop= {
    'Easy': [
      {'id': 1, 'question': 'What arithmetic operators cannot be used with strings?',
       'options': 'a) + b) *c) – d) All of the mentionedc', 'correct_answer': 4},
      {'id': 2, 'question': """What will be the output of the following Python statement? '\n' >>>print("a"+"bc") """,
       'options': '1) a 2) bc 3) bca 4) abc', 'correct_answer': 4},
      {'id': 3, 'question': """What will be the output of the following Python statement? '\n' >>>print("abcd"[2:]) """,
       'options': 'a) a  b) ab c) cd d) dc', 'correct_answer': 3},
      {'id': 4, 'question': """What will be the output of the following Python statement? '\n' >>>print(r"\nhello") """,
       'options': ' a) a new line and hello  b) \nhello  c) the letter r and then hello  d) error ',
       'correct_answer': 4},
      {'id': 5, 'question': """What will be the output of the following Python statement? '\n' "a"+"bc" """,
       'options': '1) a 2) bc 3) bca 4) abc', 'correct_answer': 2}
    ],
    'Medium': [
      {'id': 1,
       'question': """What will be the output of the following Python statement? '\n'print('abcd'.translate({97: 98, 98: 99, 99: 100})) """,
       'options': ' a) bcde b) abcd c) error  d) none of the mentioned ', 'correct_answer': 4},
      {'id': 2,
       'question': """What will be the output of the following Python statement? '\n'print('abcdefcdghcd'.split('cd', 2)) """,
       'options': ' a) [‘ab’, ‘ef’, ‘ghcd’] b) [‘ab’, ‘efcdghcd’] c) [‘abcdef’, ‘ghcd’] d) none of the mentioned ',
       'correct_answer': 1},
      {'id': 3,
       'question': """What will be the output of the following Python statement? '\n' print('ab\ncd\nef'.splitlines())  """,
       'options': ' a) [‘ab’, ‘cd’, ‘ef’] b) [‘ab\n’, ‘cd\n’, ‘ef\n’]  c) [‘ab\n’, ‘cd\n’, ‘ef’]  d) [‘ab’, ‘cd’, ‘ef\n’] ',
       'correct_answer': 1},
      {'id': 4, 'question': """What will be the output of the following Python statement? '\n' >>>print(r"\nhello") """,
       'options': ' a) AB!@ b) ab12 c) aB!2  d) aB1@ ', 'correct_answer': 3},
      {'id': 5,
       'question': """What will be the output of the following Python statement? '\n' print('ab cd ef'.title()) """,
       'options': ' a) Ab cd ef b) Ab cd eF  c) Ab Cd Ef  d) None of the mentioned ', 'correct_answer': 3}
    ],
    'Hard': [
      {'id': 1,
       'question': """What will be the output of the following Python statement? '\n  print('abcd'.translate({'a': '1', 'b': '2', 'c': '3', 'd': '4'}))  """,
       'options': ' a) abcd b) 1234  c) error d) none of the mentioned ', 'correct_answer': 1},
      {'id': 2, 'question': """What will be the output of the following Python statement? '\n'print('ab'.zfill(5))""",
       'options': ' a) 000ab  b) 00ab0 c) 0ab00 d) ab000 ', 'correct_answer': 1},
      {'id': 3,
       'question': """What will be the output of the following Python statement? '\n' print('+99'.zfill(5))   """,
       'options': ' a) [‘ab’, ‘cd’, ‘ef’] b) [‘ab\n’, ‘cd\n’, ‘ef\n’]  c) [‘ab\n’, ‘cd\n’, ‘ef’]  d) [‘ab’, ‘cd’, ‘ef\n’] ',
       'correct_answer': 1},
      {'id': 4, 'question': """What will be the output of the following Python statement? '\n' >>>print(r"\nhello") """,
       'options': ' a) 00+99 b) 0009 c) +0099  d) +++99 ', 'correct_answer': 3},
      {'id': 5,
       'question': """What will be the output of the following Python statement? '\n' print(max("what are you")) """,
       'options': ' a) error  b) u c) t  d) y   ', 'correct_answer': 4}
    ]
            }

    dict_func={
    'Easy': [
      {'id': 1, 'question': 'What arithmetic operators cannot be used with strings?',
       'options': 'a) + b) *c) – d) All of the mentionedc', 'correct_answer': 4},
      {'id': 2, 'question': """What will be the output of the following Python statement? '\n' >>>print("a"+"bc") """,
       'options': '1) a 2) bc 3) bca 4) abc', 'correct_answer': 4},
      {'id': 3, 'question': """What will be the output of the following Python statement? '\n' >>>print("abcd"[2:]) """,
       'options': 'a) a  b) ab c) cd d) dc', 'correct_answer': 3},
      {'id': 4, 'question': """What will be the output of the following Python statement? '\n' >>>print(r"\nhello") """,
       'options': ' a) a new line and hello  b) \nhello  c) the letter r and then hello  d) error ',
       'correct_answer': 4},
      {'id': 5, 'question': """What will be the output of the following Python statement? '\n' "a"+"bc" """,
       'options': '1) a 2) bc 3) bca 4) abc', 'correct_answer': 2}
    ],
    'Medium': [
      {'id': 1,
       'question': """What will be the output of the following Python statement? '\n'print('abcd'.translate({97: 98, 98: 99, 99: 100})) """,
       'options': ' a) bcde b) abcd c) error  d) none of the mentioned ', 'correct_answer': 4},
      {'id': 2,
       'question': """What will be the output of the following Python statement? '\n'print('abcdefcdghcd'.split('cd', 2)) """,
       'options': ' a) [‘ab’, ‘ef’, ‘ghcd’] b) [‘ab’, ‘efcdghcd’] c) [‘abcdef’, ‘ghcd’] d) none of the mentioned ',
       'correct_answer': 1},
      {'id': 3,
       'question': """What will be the output of the following Python statement? '\n' print('ab\ncd\nef'.splitlines())  """,
       'options': ' a) [‘ab’, ‘cd’, ‘ef’] b) [‘ab\n’, ‘cd\n’, ‘ef\n’]  c) [‘ab\n’, ‘cd\n’, ‘ef’]  d) [‘ab’, ‘cd’, ‘ef\n’] ',
       'correct_answer': 1},
      {'id': 4, 'question': """What will be the output of the following Python statement? '\n' >>>print(r"\nhello") """,
       'options': ' a) AB!@ b) ab12 c) aB!2  d) aB1@ ', 'correct_answer': 3},
      {'id': 5,
       'question': """What will be the output of the following Python statement? '\n' print('ab cd ef'.title()) """,
       'options': ' a) Ab cd ef b) Ab cd eF  c) Ab Cd Ef  d) None of the mentioned ', 'correct_answer': 3}
    ],
    'Hard': [
      {'id': 1,
       'question': """What will be the output of the following Python statement? '\n  print('abcd'.translate({'a': '1', 'b': '2', 'c': '3', 'd': '4'}))  """,
       'options': ' a) abcd b) 1234  c) error d) none of the mentioned ', 'correct_answer': 1},
      {'id': 2, 'question': """What will be the output of the following Python statement? '\n'print('ab'.zfill(5))""",
       'options': ' a) 000ab  b) 00ab0 c) 0ab00 d) ab000 ', 'correct_answer': 1},
      {'id': 3,
       'question': """What will be the output of the following Python statement? '\n' print('+99'.zfill(5))   """,
       'options': ' a) [‘ab’, ‘cd’, ‘ef’] b) [‘ab\n’, ‘cd\n’, ‘ef\n’]  c) [‘ab\n’, ‘cd\n’, ‘ef’]  d) [‘ab’, ‘cd’, ‘ef\n’] ',
       'correct_answer': 1},
      {'id': 4, 'question': """What will be the output of the following Python statement? '\n' >>>print(r"\nhello") """,
       'options': ' a) 00+99 b) 0009 c) +0099  d) +++99 ', 'correct_answer': 3},
      {'id': 5,
       'question': """What will be the output of the following Python statement? '\n' print(max("what are you")) """,
       'options': ' a) error  b) u c) t  d) y   ', 'correct_answer': 4}
    ]
  }

    dict_dict= {
    'Easy': [
      {'id': 1, 'question': 'What arithmetic operators cannot be used with strings?',
       'options': 'a) + b) *c) – d) All of the mentionedc', 'correct_answer': 4},
      {'id': 2, 'question': """What will be the output of the following Python statement? '\n' >>>print("a"+"bc") """,
       'options': '1) a 2) bc 3) bca 4) abc', 'correct_answer': 4},
      {'id': 3, 'question': """What will be the output of the following Python statement? '\n' >>>print("abcd"[2:]) """,
       'options': 'a) a  b) ab c) cd d) dc', 'correct_answer': 3},
      {'id': 4, 'question': """What will be the output of the following Python statement? '\n' >>>print(r"\nhello") """,
       'options': ' a) a new line and hello  b) \nhello  c) the letter r and then hello  d) error ',
       'correct_answer': 4},
      {'id': 5, 'question': """What will be the output of the following Python statement? '\n' "a"+"bc" """,
       'options': '1) a 2) bc 3) bca 4) abc', 'correct_answer': 2}
    ],
    'Medium': [
      {'id': 1,
       'question': """What will be the output of the following Python statement? '\n'print('abcd'.translate({97: 98, 98: 99, 99: 100})) """,
       'options': ' a) bcde b) abcd c) error  d) none of the mentioned ', 'correct_answer': 4},
      {'id': 2,
       'question': """What will be the output of the following Python statement? '\n'print('abcdefcdghcd'.split('cd', 2)) """,
       'options': ' a) [‘ab’, ‘ef’, ‘ghcd’] b) [‘ab’, ‘efcdghcd’] c) [‘abcdef’, ‘ghcd’] d) none of the mentioned ',
       'correct_answer': 1},
      {'id': 3,
       'question': """What will be the output of the following Python statement? '\n' print('ab\ncd\nef'.splitlines())  """,
       'options': ' a) [‘ab’, ‘cd’, ‘ef’] b) [‘ab\n’, ‘cd\n’, ‘ef\n’]  c) [‘ab\n’, ‘cd\n’, ‘ef’]  d) [‘ab’, ‘cd’, ‘ef\n’] ',
       'correct_answer': 1},
      {'id': 4, 'question': """What will be the output of the following Python statement? '\n' >>>print(r"\nhello") """,
       'options': ' a) AB!@ b) ab12 c) aB!2  d) aB1@ ', 'correct_answer': 3},
      {'id': 5,
       'question': """What will be the output of the following Python statement? '\n' print('ab cd ef'.title()) """,
       'options': ' a) Ab cd ef b) Ab cd eF  c) Ab Cd Ef  d) None of the mentioned ', 'correct_answer': 3}
    ],
    'Hard': [
      {'id': 1,
       'question': """What will be the output of the following Python statement? '\n  print('abcd'.translate({'a': '1', 'b': '2', 'c': '3', 'd': '4'}))  """,
       'options': ' a) abcd b) 1234  c) error d) none of the mentioned ', 'correct_answer': 1},
      {'id': 2, 'question': """What will be the output of the following Python statement? '\n'print('ab'.zfill(5))""",
       'options': ' a) 000ab  b) 00ab0 c) 0ab00 d) ab000 ', 'correct_answer': 1},
      {'id': 3,
       'question': """What will be the output of the following Python statement? '\n' print('+99'.zfill(5))   """,
       'options': ' a) [‘ab’, ‘cd’, ‘ef’] b) [‘ab\n’, ‘cd\n’, ‘ef\n’]  c) [‘ab\n’, ‘cd\n’, ‘ef’]  d) [‘ab’, ‘cd’, ‘ef\n’] ',
       'correct_answer': 1},
      {'id': 4, 'question': """What will be the output of the following Python statement? '\n' >>>print(r"\nhello") """,
       'options': ' a) 00+99 b) 0009 c) +0099  d) +++99 ', 'correct_answer': 3},
      {'id': 5,
       'question': """What will be the output of the following Python statement? '\n' print(max("what are you")) """,
       'options': ' a) error  b) u c) t  d) y   ', 'correct_answer': 4}
    ]
  }

    dictMcqTopic = {
                'str': dict_srt,
                'list': dict_list,
                'loop': dict_loop,
                'func': dict_func,
                'dict': dict_dict
                    }
    Mcq_List = [dictMcqTopic]
    """
    # print(Mcq_List[0]['str']['Medium'][0)]
    # print(Mcq_List[0]['str']['Easy'])
    """

    @classmethod
    def add_question_to_mcq_test(cls,que_type,hardness,question):

        print("quiz_que_type", que_type)
        print("quiz_hardness",hardness)
        print('questions',question)
        print(cls.Mcq_List[0][que_type][hardness][question['id']-1].update(question))

        # cls.Mcq_List[0][que_type][hardness][0]['id'] = question['id']
        # cls.Mcq_List[0][que_type][hardness][0]['question'] = question['question']
        # cls.Mcq_List[0][que_type][hardness][0]['options'] = question['options']
        # cls.Mcq_List[0][que_type][hardness][0]['correct_answer'] = question['correct_answer']
        # cls.Mcq_List[0][que_type][hardness][0].update(question)

    def __init__(self):
        # self.question= question
        # self.options= options
        # self.correct_answer = correct_answer
        self.dict_of_question = {}


    def update_question(self,id,question, options,correct_answer ):

        self.dict_of_question['id'] = id
        self.dict_of_question['question'] = question
        self.dict_of_question['options'] = options
        self.dict_of_question['correct_answer'] = correct_answer


    def add_question_to_mcq_list(self,que_type,hardness):
        quiz.add_question_to_mcq_test(question= self,que_type=que_type,hardness=hardness)

    def remove_question_from_mcq_test(self,que_type,hardness):
        quiz.Mcq_List[0][que_type][hardness].pop(self['id']-1)

    def clear_Mcq_test(self,que_type,hardness):
        quiz.Mcq_List[0][que_type][hardness].clear()

    def update_type_of_question(self,que_type,hardness):
        quiz.add_question_to_mcq_test(self,que_type,hardness)


    def type_of_question(self):
        # Type of Question
        que_type = int(input('''Mention Topic you want to take Quiz. :\n 1."str"\n 2. "list"\n 3. "loop"\n 4. "fucn"\n 5. "dict"\n  Select options:  1  2  3  4  5 :\n'''))
        list_of_topic = ['str', 'list', 'loop', 'func', 'dict']
        print("Que Type. ",list_of_topic[que_type-1], 'Selected for Quiz')

        if list_of_topic[que_type - 1] == 'str' or list_of_topic[que_type - 1] == 'list' or list_of_topic[
           que_type - 1] == 'loop' or list_of_topic[que_type - 1] == 'func' or list_of_topic[que_type - 1] == 'dict':
              # print('You have selected', list_of_topic[que_type - 1])

             return list_of_topic[que_type - 1]
        else:
            print("Pleses select corrrect option")

    def hardness_of_question(self):
        # Hardness of Question
        hardness = int(input('''\nMention Hardness of question  :\n 1. "Easy"\n 2. "Medium"\n 3. "hard :"\nSelect Options 1  2  3\n'''))
        list_of_hardness = ['Easy', 'Meduim', 'Hard']
        if list_of_hardness[hardness - 1] == 'Easy' or list_of_hardness[hardness - 1] == 'Medium' or list_of_hardness[hardness - 1] == 'Hard':
            print('Hardness of Question is : ', list_of_hardness[hardness - 1])
            return list_of_hardness[hardness - 1]
        else:
            print("Pleses select correct option")




"""

# Add first question

# print("Mention Que. Type : str   list   loop   fucn   dict")
que_type =int(input('''Mention Topic you want to take Quiz.: 1."str"   2. "list"   3. "loop"   4. "fucn"   5. "dict"  '\n' select options  1,2,3,4,5  ''' ))
list_of_topic= [ 'str', 'list', 'loop', 'func','dict']
print("que No. ", que_type)

if list_of_topic[que_type-1] == 'str' or list_of_topic[que_type-1] == 'list' or list_of_topic[que_type-1] == 'loop'  or list_of_topic[que_type-1] == 'func' or list_of_topic[que_type-1] == 'dict':
    print('You have selected', list_of_topic[que_type-1])
else:
    print("Pleses select corrrect option")



hardness =int(input('''Mention Hardness of question  : 1. "Easy"  2. "Medium"   3. "hard :"  '\n' select options 1,2,3  ''' ))

list_of_hardness = ['Easy', 'Meduim', 'Hard']

if list_of_hardness[hardness-1] == 'Easy' or list_of_hardness[hardness-1] == 'Medium' or list_of_hardness[hardness-1] == 'Hard' :
    print('You have selected', list_of_hardness[hardness-1])
else:
    print("Pleses select corrrect option")


quiz_que1 = quiz()
quiz_que1.update_question(1,'What is even NO. : ',[1,2,3,5],2)
que1 = quiz_que1.dict_of_question
quiz.add_question_to_mcq_list(que1,list_of_topic[que_type-1],list_of_hardness[hardness-1])

quiz_que2= quiz()

# print("Mention Que. Type : str   list   loop   fucn   dict")
que_type =int(input('''Mention Topic you want to take Quiz.: 1."str"   2. "list"   3. "loop"   4. "fucn"   5. "dict"  '\n' select options  1,2,3,4,5  ''' ))
list_of_topic= [ 'str', 'list', 'loop', 'func','dict']

print("que No. ", que_type)

if list_of_topic[que_type-1] == 'str' or list_of_topic[que_type-1] == 'list' or list_of_topic[que_type-1] == 'loop'  or list_of_topic[que_type-1] == 'func' or list_of_topic[que_type-1] == 'dict':
    print('You have selected', list_of_topic[que_type-1])
else:
    print("Pleses select corrrect option")



hardness =int(input('''Mention Hardness of question  : 1. "Easy"  2. "Medium"   3. "hard :"  '\n' select options 1,2,3  ''' ))

list_of_hardness = ['Easy', 'Meduim', 'Hard']

if list_of_hardness[hardness-1] == 'Easy' or list_of_hardness[hardness-1] == 'Medium' or list_of_hardness[hardness-1] == 'Hard':
    print('You have selected', list_of_hardness[hardness-1])
else:
    print("Pleses select corrrect option")



quiz_que2.update_question(2,'What is odd NO. : ',[1,2,3,5],2)
que2 = quiz_que2.dict_of_question
quiz.add_question_to_mcq_list(que2,list_of_topic[que_type-1],list_of_hardness[hardness-1])


print(quiz.Mcq_List)


print('print que 2 ',que2)
# Remove question from

quiz.remove_question_from_mcq_test(que_type= list_of_topic[que_type-1],hardness= list_of_hardness[hardness-1],self =que2)
print("Print List after removing ")
print(quiz.Mcq_List)
# Add second question


# quiz_que2 = quiz()
# quiz_que2.update_question(2, 'What is odd NO. : ',[2,4,6,7],4)
# que2 = quiz_que2.dict_of_question
# quiz.add_question_to_mcq_list(que2)


# Add third question

# quiz_que3 = quiz()
# quiz_que3.update_question(3, 'Which is not a Prime NO. : ',[1,2,3,4],4)
# que3 = quiz_que3.dict_of_question
# quiz.add_question_to_mcq_list(que3)



# Add forth question
# quiz_que4 = quiz()
# quiz_que4.update_question(4, 'Which no is divisible by 3 . : ',[4,5,6,7],3)
# que4 = quiz_que4.dict_of_question
# quiz.add_question_to_mcq_list(que4)

#................
#print(quiz.Mcq_List)


# remove question form list
# quiz.remove_question_from_mcq_test(que2)

#.......................
#print(quiz.Mcq_List)



# clear all questions from quiz
# quiz.clear_Mcq_test(quiz.Mcq_List)
# print(quiz.Mcq_List)


"""
