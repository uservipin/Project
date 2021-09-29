"""
Note Run "test_case.py"  file and follow On screen instructions
"""



dict_srt = {
    'Easy': [
        {'id': 1, 'question': 'What arithmetic operators cannot be used with strings?',
         'options': 'a) + b) *c) – d) All of the mentionedc', 'correct_answer': 4},
        {'id': 2, 'question': """What will be the output of the following Python statement? '\n' >>>print("a"+"bc") """,
         'options': '1) a 2) bc 3) bca 4) abc', 'correct_answer': 4},
        {'id': 3,
         'question': """What will be the output of the following Python statement? '\n' >>>print("abcd"[2:]) """,
         'options': 'a) a  b) ab c) cd d) dc', 'correct_answer': 3},
        {'id': 4,
         'question': """What will be the output of the following Python statement? '\n' >>>print(r"\nhello") """,
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
        {'id': 4,
         'question': """What will be the output of the following Python statement? '\n' >>>print(r"\nhello") """,
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
        {'id': 4,
         'question': """What will be the output of the following Python statement? '\n' >>>print(r"\nhello") """,
         'options': ' a) 00+99 b) 0009 c) +0099  d) +++99 ', 'correct_answer': 3},
        {'id': 5,
         'question': """What will be the output of the following Python statement? '\n' print(max("what are you")) """,
         'options': ' a) error  b) u c) t  d) y   ', 'correct_answer': 4}
    ]
}

dict_list = {
    'Easy': [
        {'id': 1, 'question': 'What arithmetic operators cannot be used with strings?',
         'options': 'a) + b) *c) – d) All of the mentionedc', 'correct_answer': 4},
        {'id': 2, 'question': """What will be the output of the following Python statement? '\n' >>>print("a"+"bc") """,
         'options': '1) a 2) bc 3) bca 4) abc', 'correct_answer': 4},
        {'id': 3,
         'question': """What will be the output of the following Python statement? '\n' >>>print("abcd"[2:]) """,
         'options': 'a) a  b) ab c) cd d) dc', 'correct_answer': 3},
        {'id': 4,
         'question': """What will be the output of the following Python statement? '\n' >>>print(r"\nhello") """,
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
        {'id': 4,
         'question': """What will be the output of the following Python statement? '\n' >>>print(r"\nhello") """,
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
        {'id': 4,
         'question': """What will be the output of the following Python statement? '\n' >>>print(r"\nhello") """,
         'options': ' a) 00+99 b) 0009 c) +0099  d) +++99 ', 'correct_answer': 3},
        {'id': 5,
         'question': """What will be the output of the following Python statement? '\n' print(max("what are you")) """,
         'options': ' a) error  b) u c) t  d) y   ', 'correct_answer': 4}
    ]
}

dict_loop = {
    'Easy': [
        {'id': 1, 'question': 'What arithmetic operators cannot be used with strings?',
         'options': 'a) + b) *c) – d) All of the mentionedc', 'correct_answer': 4},
        {'id': 2, 'question': """What will be the output of the following Python statement? '\n' >>>print("a"+"bc") """,
         'options': '1) a 2) bc 3) bca 4) abc', 'correct_answer': 4},
        {'id': 3,
         'question': """What will be the output of the following Python statement? '\n' >>>print("abcd"[2:]) """,
         'options': 'a) a  b) ab c) cd d) dc', 'correct_answer': 3},
        {'id': 4,
         'question': """What will be the output of the following Python statement? '\n' >>>print(r"\nhello") """,
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
        {'id': 4,
         'question': """What will be the output of the following Python statement? '\n' >>>print(r"\nhello") """,
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
        {'id': 4,
         'question': """What will be the output of the following Python statement? '\n' >>>print(r"\nhello") """,
         'options': ' a) 00+99 b) 0009 c) +0099  d) +++99 ', 'correct_answer': 3},
        {'id': 5,
         'question': """What will be the output of the following Python statement? '\n' print(max("what are you")) """,
         'options': ' a) error  b) u c) t  d) y   ', 'correct_answer': 4}
    ]
}

dict_func = {
    'Easy': [
        {'id': 1, 'question': 'What arithmetic operators cannot be used with strings?',
         'options': 'a) + b) *c) – d) All of the mentionedc', 'correct_answer': 4},
        {'id': 2, 'question': """What will be the output of the following Python statement? '\n' >>>print("a"+"bc") """,
         'options': '1) a 2) bc 3) bca 4) abc', 'correct_answer': 4},
        {'id': 3,
         'question': """What will be the output of the following Python statement? '\n' >>>print("abcd"[2:]) """,
         'options': 'a) a  b) ab c) cd d) dc', 'correct_answer': 3},
        {'id': 4,
         'question': """What will be the output of the following Python statement? '\n' >>>print(r"\nhello") """,
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
        {'id': 4,
         'question': """What will be the output of the following Python statement? '\n' >>>print(r"\nhello") """,
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
        {'id': 4,
         'question': """What will be the output of the following Python statement? '\n' >>>print(r"\nhello") """,
         'options': ' a) 00+99 b) 0009 c) +0099  d) +++99 ', 'correct_answer': 3},
        {'id': 5,
         'question': """What will be the output of the following Python statement? '\n' print(max("what are you")) """,
         'options': ' a) error  b) u c) t  d) y   ', 'correct_answer': 4}
    ]
}

dict_dict = {
    'Easy': [
        {'id': 1, 'question': 'What arithmetic operators cannot be used with strings?',
         'options': 'a) + b) *c) – d) All of the mentionedc', 'correct_answer': 4},
        {'id': 2, 'question': """What will be the output of the following Python statement? '\n' >>>print("a"+"bc") """,
         'options': '1) a 2) bc 3) bca 4) abc', 'correct_answer': 4},
        {'id': 3,
         'question': """What will be the output of the following Python statement? '\n' >>>print("abcd"[2:]) """,
         'options': 'a) a  b) ab c) cd d) dc', 'correct_answer': 3},
        {'id': 4,
         'question': """What will be the output of the following Python statement? '\n' >>>print(r"\nhello") """,
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
        {'id': 4,
         'question': """What will be the output of the following Python statement? '\n' >>>print(r"\nhello") """,
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
        {'id': 4,
         'question': """What will be the output of the following Python statement? '\n' >>>print(r"\nhello") """,
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